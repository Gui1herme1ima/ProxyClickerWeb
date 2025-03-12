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


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_clicks', methods=['POST'])
def start_clicks():
    url = request.form['url']
    num_cliques_desejados = int(request.form['num_cliques'])
    tempo = float(request.form['tempo_medio'])

    cliques_concluidos = 0
    tentativas_totais = 0

    # Aloca uma proxy para a sessão
    
    proxy_info = proxies_available.pop(0)  # Remove a primeira proxy disponível
    print(f"-----------------------------------------------------------------\n{proxy_info['usuario']}")

    while cliques_concluidos < num_cliques_desejados:

        headers = random.choice(headers_list)
        proxy = f"http://{proxy_info['usuario']}-session-{random.randint(1, 1000)}:{proxy_info['senha']}@{proxy_info['host']}:{proxy_info['porta']}"

        # Realiza o clique
        try:
            response = requests.get(
                url,
                headers=headers,
                proxies={"http": proxy, "https": proxy},
                timeout=10,
                verify=False
            )
            if response.status_code == 200:
                cliques_concluidos += 1
                message = f"Clique concluído com sucesso!"
            else:
                message = f"Erro no clique. Status Code: {response.status_code}"
        except Exception as e:
            message = f"Erro: {e}"

        tentativas_totais += 1
        print(f"Tentativa {tentativas_totais}: {message}")

        # Simula o tempo de espera
        time.sleep(tempo)
        print(f"Aguardando {tempo} segundos...")

        # Libera a proxy após a conclusão dos cliques
        with proxies_lock:
            proxies_available.append(proxy_info)

        return jsonify({
            "message": message,
            "cliques_concluidos": cliques_concluidos
        })
