from bs4 import BeautifulSoup
from collections import Counter
import requests
import operator

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''

      
   _____                    _             _  __             _____                     _ 
  / ____|                  | |           | |/ /            / ____|                   | |
 | |     _ __ __ ___      _| | ___ _ __  | ' / ___ _   _  | |  __ _   _  __ _ _ __ __| |
 | |    | '__/ _` \ \ /\ / / |/ _ \ '__| |  < / _ \ | | | | | |_ | | | |/ _` | '__/ _` |
 | |____| | | (_| |\ V  V /| |  __/ |    | . \  __/ |_| | | |__| | |_| | (_| | | | (_| |
  \_____|_|  \__,_| \_/\_/ |_|\___|_|    |_|\_\___|\__, |  \_____|\__,_|\__,_|_|  \__,_|
                                                    __/ |                               
                                                   |___/                                

                                               
''' + RESET)

# Exemplo de site para teste: "https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar"

def start(url):

    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "html.parser")

    # O texto em determinada página da web é armazenado em
    # As tags <div> com classe <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):

    clean_list = []

    for word in wordlist:
        symbols = '!@#$%^&*()_+={[]}|\;:.,"<>?/-'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    
    create_dictionary(clean_list)

def create_dictionary(clean_list):

    word_count = {}

    for word in clean_list:
        
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s" % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print("\n")
    print(top)
    print("\n")

if __name__ == "__main__":
    start(input("Informe o site que você deseja extrair as palavras-chave: "))