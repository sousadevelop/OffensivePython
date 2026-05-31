# Permite trabalhar com calculos e somas de IPs, alem de redes.
# Os enderecos abaixo pertencem ao bloco reservado para documentacao.

import ipaddress

ip = "192.0.2.1"

ip = ipaddress.ip_address(ip)

print(ip + 10)
print("-" * 100)


###########################################################################

ip_rede = "192.0.2.0/29"

rede = ipaddress.ip_network(ip_rede)

for ip in rede:
    print(ip)
