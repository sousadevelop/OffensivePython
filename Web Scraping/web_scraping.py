from bs4 import BeautifulSoup
import requests

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''

   ___           _                   __                      _             
  / __\   _ _ __(_) ___  _   _ ___  / _\ ___ _ __ __ _ _ __ (_)_ __   __ _ 
 / / | | | | '__| |/ _ \| | | / __| \ \ / __| '__/ _` | '_ \| | '_ \ / _` |
/ /__| |_| | |  | | (_) | |_| \__ \ _\ \ (__| | | (_| | |_) | | | | | (_| |
\____/\__,_|_|  |_|\___/ \__,_|___/ \__/\___|_|  \__,_| .__/|_|_| |_|\__, |
                                                      |_|            |___/ 
                                                             

                                               
''' + RESET)

link = input("""Digite o site que deseja analisar.\n 
Exemplo: http://www.site.com.br/\n
->  """)

# O objeto link receberá o conteúdo da requisição http do site informado no input...
requisicao = requests.get(link).content

# O objeto soup irá baixar o HTML do site
soup = BeautifulSoup(requisicao, "html.parser")

# print(soup.prettify())      # a função prettify() transforma o HTML em string

print(soup.find_all("a"), "\n")
print(BLUE + "~~" * 100, "\n" + RESET)
print(soup.find_all("admin"), "\n")
print(BLUE + "~~" * 100, "\n" + RESET)
print(soup.find_all("password"), "\n")