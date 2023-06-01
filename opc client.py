# -*- coding: utf-8 -*-
"""
Created on Mon May 29 13:28:51 2023

@author: AlecFreire
"""

import requests
from opcua import Client
from datetime import datetime
import time

# Cria um cliente OPC UA
url = "opc.tcp://localhost:4840"
client = Client(url)

# Conecta ao servidor OPC UA
client.connect()

# Obtém o objeto de nó para a variável de temperatura
temperature_node = client.get_node("ns=2;i=2")
temperature_node2 = client.get_node("ns=2;i=3")
temperature_node3 = client.get_node("ns=2;i=4")
# ...

# URL da plataforma web
web_url = "http://localhost:5000/api/endpoint"

# Loop para exibir as temperaturas e enviar para a plataforma web a cada 10 segundos
while True:
    # Lê os valores das variáveis de temperatura
    temperature1 = temperature_node.get_value()
    temperature2 = temperature_node2.get_value()
    temperature3 = temperature_node3.get_value()

    # Obtém o timestamp atual
    timestamp = datetime.now().isoformat()

    # Exibe as temperaturas e o timestamp
    print("Timestamp: {}".format(timestamp))
    print("Temperatura 1: {} graus Celsius".format(temperature1))
    print("Temperatura 2: {} graus Celsius".format(temperature2))
    print("Temperatura 3: {} graus Celsius".format(temperature3))

    # Dados a serem enviados para a plataforma web
    data = {
        "timestamp": timestamp,
        "temperature1": temperature1,
        "temperature2": temperature2,
        "temperature3": temperature3
    }

    # Realiza a requisição POST para a plataforma web
    response = requests.post(web_url, json=data)
    
    # Print the response
    # response_json = response.json()
    # print(response_json)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        print("Dados enviados com sucesso!")
    else:
        print("Erro ao enviar os dados:", response.status_code)
        
    # Aguarda 10 segundos antes da próxima iteração
    time.sleep(10)
