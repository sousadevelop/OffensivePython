import socket           # API do Sistema Operacional que permite a comunicação com a placa de rede

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''

 __    __                 __                 
/ / /\ \ \__ _ _ __ ___  / _\ ___ __ _ _ __  
\ \/  \/ / _` | '__/ _ \ \ \ / __/ _` | '_ \ 
 \  /\  / (_| | | |  __/ _\ \ (_| (_| | | | |
  \/  \/ \__,_|_|  \___| \__/\___\__,_|_| |_|
                                                                    
                                               
''' + RESET)

ip = input("Digite o IP ou Host: ")

qtd = int(input("Informe quantas portas você deseja scannear: "))

ports = []
count = 0

while count < qtd:
    ports.append(int(input("Digite a porta: ")))
    count += 1

for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)                   # Configura o tempo de resposta da requisição
    code = cliente.connect_ex((ip, port))

    if code == 0:
        print(BLUE + f"\nPorta {port} - [ Aberta ]" + RESET)
    else:
        print(RED + f"\nPorta {port} - [ Fechada ]" + RESET)