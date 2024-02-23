import random
import string

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''

   ___                                    _                _        
  / _ \__ _ ___ _____      _____  _ __ __| |   /\/\   __ _| | _____ 
 / /_)/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  /    \ / _` | |/ / _ \
/ ___/ (_| \__ \__ \\ V  V / (_) | | | (_| | / /\/\ \ (_| |   <  __/
\/    \__,_|___/___/ \_/\_/ \___/|_|  \__,_| \/    \/\__,_|_|\_\___|
                                                                    
                                               
''' + RESET)

size = int(input("Digite o tamanho que deseja para sua senha: "))

chars = string.ascii_letters + string.digits + "!@#$%&*()_+=/-|?,.<>;:[]"

rnd = random.SystemRandom()

print("*" * 50)
print("\n")
print("SENHA: \n")
print(BLUE + "".join(rnd.choice(chars) for i in range(size)) + RESET)
print("\n")
print("*" * 50)