from flask import render_template, request, jsonify
from app import app
from headers import headers_list
import proxies
import random
import requests
from urllib3.exceptions import InsecureRequestWarning
from threading import Lock
import time

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

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

def get_proxy_ipinfo(proxy):
    """
    Obtém o IP externo usando a proxy fornecida.
    """
    try:
        response = requests.get(
            'https://ipinfo.io/json',
            proxies={"http": proxy, "https": proxy},
            timeout=10,
            verify=False
        )
        response.raise_for_status()
        ip_data = response.json()
        return ip_data.get('ip')
    except Exception as e:
        print(f"Erro ao obter IP da proxy {proxy}: {e}")
        return None
    
def get_proxy_ipify(proxy):
    """
    Obtém o IP externo usando a proxy fornecida.
    """
    try:
        response = requests.get(
            'https://api64.ipify.org?format=json',
            proxies={"http": proxy, "https": proxy},
            timeout=10,
            verify=False
        )
        response.raise_for_status()
        ip_data = response.json()
        return ip_data.get('ip')
    except Exception as e:
        print(f"Erro ao obter IP da proxy {proxy}: {e}")
        return None

def get_proxy_ipapi(proxy):
    """
    Obtém o IP externo usando a proxy fornecida.
    """
    try:
        response = requests.get(
            'http://ip-api.com/json/',
            proxies={"http": proxy, "https": proxy},
            timeout=10,
            verify=False
        )
        response.raise_for_status()
        ip_data = response.json()
        return ip_data.get('query')
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
    android_cliques = int(request.form['android_cliques'])
    iphone_cliques = int(request.form['iphone_cliques'])

    print(android_cliques)
    print(iphone_cliques)

    cliques_concluidos = 0
    tentativas_totais = 0
    ultimo_dispositivo = None  # Controla o último dispositivo usado

    while cliques_concluidos < num_cliques_desejados:

        # Bloqueia o acesso à fila de proxies para garantir thread-safety
        with proxies.proxy_lock:
            if not proxies.proxies_queue.empty():
                proxy_info = proxies.proxies_queue.get()  # Obtém a próxima proxy disponível
            else:
                print("Proxys em cooldown, aguarde...")
                time.sleep(5)
                continue

        print(f"------------------------------------------------------------\nProxy selecionada: {proxy_info['id']}")
        
        # Monta a string da proxy
        proxy = f"http://{proxy_info['usuario']}-session-{random.randint(1, 1000)}:{proxy_info['senha']}@{proxy_info['host']}:{proxy_info['porta']}"

        # Obtém o IP da proxy
        proxyAPI =random.choice([1,2,3])
        
        if proxyAPI == 1:
            proxy_ip = get_proxy_ipinfo(proxy)
            print("API: IPinfo")
        elif proxyAPI == 2:
            proxy_ip = get_proxy_ipify(proxy)
            print("API: IPify")
        else:
            proxy_ip = get_proxy_ipapi(proxy)
            print("API: IP-API")

        # Verifica se o IP é do Brasil e obtém a cidade
        country, city = get_ip_geolocation(proxy_ip)
        if country not in ["BR"]:
            print(f"Proxy com IP {proxy_ip} não é do Brasil ({country}, {city}). Buscando nova proxy...")

            # Libera a proxy de volta para a fila (pois não será usada)
            with proxies.proxy_lock:
                proxies.proxies_queue.put(proxy_info)
        
            continue  # Volta ao início do loop para buscar uma nova proxy

        print(f"Proxy com IP {proxy_ip} é do Brasil ({city}). Prosseguindo...")

        # Seleciona o dispositivo (Android ou iPhone)
        if android_cliques > 0 and iphone_cliques > 0:
            headers = random.choice(headers_list)
            print(headers)

            if 'android' in headers['User-Agent'].lower():
                dispositivo = 'android'
            elif 'iphone' in headers['User-Agent'].lower():
                dispositivo = 'iphone'
            else:
                continue
        
        elif android_cliques > 0 and iphone_cliques == 0:
            dispositivo = 'android'
            headers = random.choice([h for h in headers_list if dispositivo in h['User-Agent'].lower()])

        elif android_cliques == 0 and iphone_cliques > 0:
            dispositivo = 'iphone'
            headers = random.choice([h for h in headers_list if dispositivo in h['User-Agent'].lower()])
        else:
            break  # Todos os cliques foram concluídos

        # Seleciona um header correspondente ao dispositivo

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

        # Libera a proxy de volta para a fila após o uso
        with proxies.proxy_lock:
            proxies.proxies_queue.put(proxy_info)

        return jsonify({
        "message": message,
        "cliques_concluidos": cliques_concluidos,
        "dispositivo": dispositivo
})
