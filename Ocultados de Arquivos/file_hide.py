## Lab local de esteganografia com texto ficticio. ##

from stegano import lsb

# Cores
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + "Lab local de esteganografia" + RESET)

# Use somente imagens de laboratorio e mensagens ficticias.
placeholder_message = "LAB_PLACEHOLDER_MESSAGE"
secret = lsb.hide("./pexels-anton-atanasov-213172.png", placeholder_message)
secret.save("./life_secret.example.png")

# Revelando o texto oculto no arquivo gerado localmente:
# awake_true = lsb.reveal("./life_secret.example.png")
# print(awake_true)
