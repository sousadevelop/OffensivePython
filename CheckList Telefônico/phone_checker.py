import phonenumbers
from phonenumbers import geocoder       # Trás a localização do telefone
from phonenumbers import carrier 
from phonenumbers import timezone 

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''


  _______   _            _                                             _                    
 |__   __| | |          | |                          /\               | |                   
    | | ___| | ___ _ __ | |__   ___  _ __   ___     /  \   _ __   __ _| |_   _ _______ _ __ 
    | |/ _ \ |/ _ \ '_ \| '_ \ / _ \| '_ \ / _ \   / /\ \ | '_ \ / _` | | | | |_  / _ \ '__|
    | |  __/ |  __/ |_) | | | | (_) | | | |  __/  / ____ \| | | | (_| | | |_| |/ /  __/ |   
    |_|\___|_|\___| .__/|_| |_|\___/|_| |_|\___| /_/    \_\_| |_|\__,_|_|\__, /___\___|_|   
                  | |                                                     __/ |             
                  |_|                                                    |___/              
                                                             
                                            
''' + RESET)

phone = input("Informe o número de telefone que você deseja localizar no seguinte formato: ex.: +5531988428465\n-> ")

# Aqui a função parse irá converter a string em número de telefone
phone_number = phonenumbers.parse(phone)        

# Aqui ele vai informar a localização por estado do país e no idioma "pt" que é português
state = geocoder.description_for_number(phone_number, 'pt')

# Trás o fuso horário da localização do telefone
timeZone = timezone.time_zones_for_number(phone_number) 

# Busca a operadora do número de telefone 
Carrier = carrier.name_for_number(phone_number, 'pt') 
  
# Informa a região 
Region = geocoder.description_for_number(phone_number, 'pt') 

# Verifica se está em uma central atribuída 
valid = phonenumbers.is_valid_number(phone_number) 
  
# Verifica se tem a quantidade correta de dígitos para um número telefônico
possible = phonenumbers.is_possible_number(phone_number) 
  
# Exibe as informações
print(f"{BLUE}\nO estado em que se encontra é {state}.\n{RESET}")
print(f"{BLUE}O seu fuso horário é {timeZone}.\n{RESET}")
print(f"{BLUE}A sua Operadora telefônica é {Carrier}.\n{RESET}") 
print(f"{BLUE}A sua Região Geográfica é {Region}.\n{RESET}") 
print(f"{BLUE}O número informado está {valid} para uma Central telefônica.\n{RESET}") 
print(f"{BLUE}O número informado é {possible} para usar como número telefônico, pois tem a quantidade esperada de dígitos.{RESET}\n") 