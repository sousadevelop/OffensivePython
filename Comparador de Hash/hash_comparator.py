import hashlib

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m" 
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + """

  _    _           _       ______                    _____                     _ 
 | |  | |         | |     |  ____|                  / ____|                   | |
 | |__| | __ _ ___| |__   | |__ ___  _ __ ___ ___  | |  __ _   _  __ _ _ __ __| |
 |  __  |/ _` / __| '_ \  |  __/ _ \| '__/ __/ _ \ | | |_ | | | |/ _` | '__/ _` |
 | |  | | (_| \__ \ | | | | | | (_) | | | (_|  __/ | |__| | |_| | (_| | | | (_| |
 |_|  |_|\__,_|___/_| |_| |_|  \___/|_|  \___\___|  \_____|\__,_|\__,_|_|  \__,_|
                                                                                 
                                                                                 

""" + RESET)

file_1 = input("Digite o hash que deseja identificar: ").lower()
file_2 = 'rockyou.txt'

with open(file_2, 'rb') as file:
    for line in file:
        line = line.rstrip(b'\r\n')  # Remove os caracteres de nova linha
        hash_2 = hashlib.sha512(line)

        if file_1 != hash_2.hexdigest():
            print(f"\nO hash 1 ({BLUE} {file_1} {RESET}) \n\né DIFERENTE \n\ndo hash 2 ({RED} {hash_2.hexdigest()} {RESET})\n")
            print("~~" * 70)
        else:
            print(f"O hash 1 ({BLUE} {file_1} {RESET}) \n\né IGUAL \n\ndo hash 2 ({BLUE} {hash_2.hexdigest()} {RESET})")
            break 