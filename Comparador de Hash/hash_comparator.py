import hashlib

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m" 
RESET = "\033[0;0m"

file_1 = input("Digite o hash que deseja identificar: ")
file_2 = 'two.txt'

for line in open(file_2, 'rb'):

    hash_1 = hashlib.new('sha512')
    hash_1.update(file_1.encode('utf-8'))

    hash_2 = hashlib.new('sha512')
    hash_2.update(line)

    if hash_1.digest() != hash_2.digest():

        print(f"\nO hash 1 ({BLUE} {hash_1.hexdigest()} {RESET}) \n\né DIFERENTE \n\ndo hash 2 ({RED} {hash_2.hexdigest()} {RESET})\n")
        print("~~" * 70)

    else:

        print(f"O hash 1 ({BLUE} {hash_1.hexdigest()} {RESET}) \n\né IGUAL \n\ndo hash 2 ({BLUE} {hash_2.hexdigest()} {RESET})")
        break