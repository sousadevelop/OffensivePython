import random
import string

# Cores
BLUE  = "\033[1;34m"
RESET = "\033[0;0m"

size = int(input("Digite o tamanho que deseja para sua senha: "))

chars = string.ascii_letters + string.digits + "!@#$%&*()_+=/-|?,.<>;:[]"

rnd = random.SystemRandom()

print("*" * 50)
print("\n")
print("SENHA: \n")
print(BLUE + "".join(rnd.choice(chars) for i in range(size)) + RESET)
print("\n")
print("*" * 50)