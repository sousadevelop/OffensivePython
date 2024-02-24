import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = input("Digite o host ou IP que deseja verificar se está ativo: ")
porta = input("Digite a porta/serviço que deseja validar: ")

s.bind((host, int(porta)))       # Faz uma ligação com o objeto de conexão usando o host e a porta
mensagem = input("Digite a mensagem que deseja enviar para o cliente: ")
mensagem = f"\n{mensagem}"

while True:
    dados, address = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), address)