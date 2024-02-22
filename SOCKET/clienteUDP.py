# A conexão UDP foca no princípio da DISPONIBILIDADE

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso! 😎")

host = input("Digite o host ou IP que deseja verificar se está ativo: ")
porta = input("Digite a porta/serviço que deseja validar: ")
mensagem = input("Digite a mensagem que deseja enviar para o servidor: ")

try:

    print(f"Cliente: {mensagem}")
    s.sendto(mensagem.encode(), (host, int(porta)))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")

finally:

    print("Cliente: fechando a conexão. 🔒")
    s.close()