# -*- coding: utf-8 -*-
"""
Created on Mon May 29 13:25:54 2023

@author: AlecFreire
"""

from opcua import ua, Server
import random
import time

# Inicializa o servidor OPC UA
server = Server()
url = "opc.tcp://localhost:4840"
server.set_endpoint(url)

# Cria um espaço de nomes
namespace = server.register_namespace("TemperatureSimulation")

# Cria um objeto de nó raiz
root_node = server.get_objects_node()

# Cria um objeto de nó filho para as variáveis de temperatura
temperature_node = root_node.add_object(namespace, "Temperature")

# Cria uma variável de temperatura
temperature_variable1 = temperature_node.add_variable(namespace, "Temperature 1", 0)
temperature_variable2 = temperature_node.add_variable(namespace, "Temperature 2", 0)
temperature_variable3 = temperature_node.add_variable(namespace, "Temperature 3", 0)

# Configura as propriedades da variável de temperatura
temperature_variable1.set_writable()
temperature_variable2.set_writable()
temperature_variable3.set_writable()

# Inicia o servidor OPC UA
server.start()

# Loop para simular as variáveis de temperatura
while True:
    # Gera um valor aleatório entre 100 e 200
    temperature1 = random.uniform(100, 200)
    temperature2 = random.uniform(100, 200)
    temperature3 = random.uniform(100, 200)

    # Atualiza o valor da variável de temperatura no servidor
    temperature_variable1.set_value(temperature1)
    temperature_variable2.set_value(temperature2)
    temperature_variable3.set_value(temperature3)

    # Aguarda um intervalo de tempo
    time.sleep(1)

