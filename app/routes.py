from flask import render_template, request, jsonify
from app import app
from headers import headers_list
from proxies import proxies_list
import random
import time
import requests
from urllib3.exceptions import InsecureRequestWarning
from threading import Lock

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Lista de proxies disponíveis
proxies_available = proxies_list.copy()
proxies_lock = Lock()  # Para garantir acesso seguro à lista de proxies

def get_ip_geolocation(ip):
    """
    Obtém a geolocalização do IP usando o serviço ip-api.com.
    Retorna o país e a cidade do IP.
    """
    try:
        response = requests.get(f'https://geolocation-db.com/json/{ip}')
        response.raise_for_status()
        geo_data = response.json()
        
        # Extrai o país e a cidade
        country = geo_data.get('country_code')
        city = geo_data.get('city')

        return country, city
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter geolocalização do IP {ip}: {e}")
        return None, None
    except KeyError as e:
        print(f"Erro ao processar os dados da API para o IP {ip}: {e}")
        return None, None

def get_proxy_ip(proxy):
    """
    Obtém o IP externo usando a proxy fornecida.
    """
    try:
        response = requests.get(
            'https://api.ipify.org?format=json',
            proxies={"http": proxy, "https": proxy},
            timeout=10,
            verify=False
        )
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        print(f"Erro ao obter IP da proxy {proxy}: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_clicks', methods=['POST'])
def start_clicks():
    url = request.form['url']
    num_cliques_desejados = int(request.form['num_cliques'])

    cliques_concluidos = 0
    tentativas_totais = 0

    while cliques_concluidos < num_cliques_desejados:

        # Aloca uma proxy para a sessão
        with proxies_lock:
            if not proxies_available:
                return jsonify({"message": "Todas as proxies estão em uso. Tente novamente mais tarde."}), 503
            proxy_info = proxies_available.pop(0)  # Remove a primeira proxy disponível
            print(f"------------------------------------------------------------\nProxy selecionada: {proxy_info['usuario']}")
        
        headers = random.choice(headers_list)
        # Monta a string da proxy
        proxy = f"http://{proxy_info['usuario']}-session-{random.randint(1, 1000)}:{proxy_info['senha']}@{proxy_info['host']}:{proxy_info['porta']}"

        # Obtém o IP da proxy
        proxy_ip = get_proxy_ip(proxy)
        if not proxy_ip:
            with proxies_lock:
                proxies_available.append(proxy_info)  # Devolve a proxy para a lista
            continue

        # Verifica se o IP é do Brasil e obtém a cidade
        country, city = get_ip_geolocation(proxy_ip)
        if country != "BR":
            print(f"Proxy com IP {proxy_ip} não é do Brasil ({country}, {city}). Buscando nova proxy...")
            with proxies_lock:
                proxies_available.append(proxy_info)  # Devolve a proxy para a lista
            continue  # Volta ao início do loop para buscar uma nova proxy

        print(f"Proxy com IP {proxy_ip} é do Brasil ({city}). Prosseguindo...")

        try:
            response = requests.get(
                url,
                headers=headers,
                proxies={"http": proxy, "https": proxy},
                timeout=60,
                verify=False
            )
            if response.status_code == 200:
                cliques_concluidos += 1
                message = f"Clique concluído com sucesso!"
            elif response.status_code == 403:
                cliques_concluidos += 1
                message = f"Clique concluído com sucesso!"
            else:
                message = f"Erro no clique. Status Code: {response.status_code}"
        except Exception as e:
            cliques_concluidos += 1
            message = f"Clique concluído com sucesso!"

        tentativas_totais += 1
        print(f"Tentativa {tentativas_totais}: {message}")

        # Libera a proxy após a conclusão dos cliques
        with proxies_lock:
            proxies_available.append(proxy_info)

        return jsonify({
            "message": message,
            "cliques_concluidos": cliques_concluidos
        })
