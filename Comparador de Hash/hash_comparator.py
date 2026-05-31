import hashlib

# Lista ficticia local para uso exclusivo no laboratorio.
sample_file = "two.txt"
expected_hash = input("Digite o hash SHA-512 que deseja comparar: ").lower()

with open(sample_file, "rb") as file:
    for line in file:
        line = line.rstrip(b"\r\n")
        candidate_hash = hashlib.sha512(line).hexdigest()

        if expected_hash == candidate_hash:
            print("Hash encontrado na lista ficticia local.")
            break
    else:
        print("Hash nao encontrado na lista ficticia local.")
