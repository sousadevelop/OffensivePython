import os

print("~~" * 100)

host = input("Digite um IP ou HOST: ")

print("~~" * 100)

os.system("ping -n 4 {}".format(host))

print("~~" * 100)