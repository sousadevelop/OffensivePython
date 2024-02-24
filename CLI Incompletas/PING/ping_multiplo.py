import os
import time

# Cores
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
RESET = "\033[0;0m"

sites = 'hosts.txt'
print(os.getcwd())

with open(sites) as file:
    dump = file.read()
    dump = dump.splitlines()            # Separa por linhas como está escrito no arquivo

    for ip in dump:
        print(RED + 'Verificando o IP: ', ip + RESET)
        print(BLUE + '~~' * 100 + RESET)
        os.system("ping -n 3 {}".format(ip))
        print(BLUE + '~~' * 100 + RESET)
        time.sleep(4)