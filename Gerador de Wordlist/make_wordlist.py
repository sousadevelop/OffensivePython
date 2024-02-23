import itertools

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''

              _          __    __              _ _ _     _   
  /\/\   __ _| | _____  / / /\ \ \___  _ __ __| | (_)___| |_ 
 /    \ / _` | |/ / _ \ \ \/  \/ / _ \| '__/ _` | | / __| __|
/ /\/\ \ (_| |   <  __/  \  /\  / (_) | | | (_| | | \__ \ |_ 
\/    \/\__,_|_|\_\___|   \/  \/ \___/|_|  \__,_|_|_|___/\__|
                                                             

                                               
''' + RESET)

string = input("Digite a string que será permutada, isto é, usada para gerar uma wordlist: ")

length = int(input("Digite o número do tamanho das linhas da wordlist: "))

result = itertools.permutations(string, length)

qtd_lines = len(string) * length

print("\n")
print(BLUE + f"A quantidade de linhas geradas será: {qtd_lines}" + RESET)
print("\n")

for line in result:
    print(''.join(line))