# A conexão TCP foca no princípio da INTEGRIDADE

import socket
import sys

blue = '\033[1;36;40m'


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)        # o 0/zero representa conexão TCP
    
    except socket.error as e:
        print("A conexão falhou! 😥 ")
        print("Erro: {}".format(e))
        sys.exit()

    print(f"{blue}Socket criado com sucesso! 😁")

    HostAlvo = input("Digite o Host ou IP que deseja se conectar: ")
    PortaAlvo = input("Digite a Porta que deseja testar: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f"Cliente TCP conectado com Sucesso no Host: {HostAlvo} e na Porta: {PortaAlvo}")
        s.shutdown(2)

    except socket.error as e:
        print(f"Não foi possível se conectar no Host e na Porta: {HostAlvo} - {PortaAlvo}")
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()