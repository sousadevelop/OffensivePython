import hashlib

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''
              _                          _     
  /\/\   __ _| | _____    /\  /\__ _ ___| |__  
 /    \ / _` | |/ / _ \  / /_/ / _` / __| '_ \ 
/ /\/\ \ (_| |   <  __/ / __  / (_| \__ \ | | |
\/    \/\__,_|_|\_\___| \/ /_/ \__,_|___/_| |_|
                                               
''' + RESET)

string = input("Digite o texto que deseja transformar em hash: ")
# string = print(b"Python cool") -> o 'b' antes das aspas torna o texto em binário

menu = int(input(BLUE + '''         \nMENU - ESCOLHA O TIPO DE HASH
                 1 - MD5
                 2 - SHA1
                 3 - SHA224
                 4 - SHA256
                 5 - SHA512
Digite um número para informar para qual formato de hash deseja converter o texto: ''' + RESET))

if menu == 1:
    resultado = hashlib.md5(string.encode("utf-8"))             # a função .encode("utf-8") converte uma variável para ser aceita
    print(f"\nO hash MD5 da string {string} é -> {resultado.hexdigest()}")
elif menu == 2:
    resultado = hashlib.sha1(string.encode("utf-8"))
    print(f"\nO hash sha1 da string {string} é -> {resultado.hexdigest()}")
elif menu == 3:
    resultado = hashlib.sha224(string.encode("utf-8"))
    print(f"\nO hash sha224 da string {string} é -> {resultado.hexdigest()}")
elif menu == 4:
    resultado = hashlib.sha256(string.encode("utf-8"))
    print(f"\nO hash sha256 da string {string} é -> {resultado.hexdigest()}")
elif menu == 5:
    resultado = hashlib.sha512(string.encode("utf-8"))
    print(f"\nO hash sha512 da string {string} é -> {resultado.hexdigest()}")
else:
    print(RED + "\nO texto e/ou o número informado não puderam ser compreendido. Tente novamente, por favor." + RESET)