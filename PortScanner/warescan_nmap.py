import nmap

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

scanner = nmap.PortScanner()

print(CYAN + "Seja bem-vindo !!" + RESET)
print("\n<------------------------>\n")

ip = input("Digite o IP ou Host que deseja scannear: ")
print(f"O IP digitado foi: {ip}")
type(ip)

menu = input("""\n Escolha o tipo de varredura a ser realizado:
             1 -> Varredura do tipo SYN
             2 -> Varredura do tipo UDP
             3 -> Varredura do tipo TCP Intenso
             Digite o tipo de varredura que deseja usar: """)
print(BLUE + f"\nA opção escolhida foi: {menu}\n" + RESET)

if menu == "1":
    print(f"Versão do Nmap: {scanner.nmap_version()}")
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
elif menu == "2":
    print(f"Versão do Nmap: {scanner.nmap_version()}")
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print("")
    protocols = scanner[ip].all_protocols()
    if 'udp' in protocols:
        print("Portas Abertas: ", scanner[ip]['udp'].keys())
    else:
        print( "Não há informações sobre portas UDP disponíveis para este IP.")
elif menu == "3":
    print(f"Versão do Nmap: {scanner.nmap_version()}")
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
else:
    print(RED + "A opção informada não é possível ser aceita. 🙁" + RESET)