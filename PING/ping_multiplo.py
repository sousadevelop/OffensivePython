import os
import time

blue = '\033[1;36;40m'
green = '\033[1;36;42m'

sites = 'hosts.txt'
print(os.getcwd())

with open(sites) as file:
    dump = file.read()
    dump = dump.splitlines()            # Separa por linhas como está escrito no arquivo

    for ip in dump:
        print(f'{green}Verificando o IP: ', ip)
        print(f'{blue}~~' * 100)
        os.system("ping -n 3 {}".format(ip))
        print(f'{blue}~~' * 100)
        time.sleep(4)