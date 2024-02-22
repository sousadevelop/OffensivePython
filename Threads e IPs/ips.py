# Permite trabalhar com cálculos e somas de IPs, além de redes.

import ipaddress

ip = "192.168.0.1"

ip = ipaddress.ip_address(ip)       # Converte a string em IP

print(ip + 256)         # Cálculo de IP
print("-" * 100)


###########################################################################

ip_rede = "192.168.0.0/24"

rede = ipaddress.ip_network(ip_rede)    # Caso queira que aceite qualquer IP e converta para o mais próximo, use: (ip_rede, strict=False)

for ip in rede:
    print(ip)