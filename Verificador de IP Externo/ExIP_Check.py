import re
import json
from urllib.request import urlopen

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''


   _____ _               _    _               ______      _                        _   _____ _____    _____        __                           _   _             
  / ____| |             | |  (_)             |  ____|    | |                      | | |_   _|  __ \  |_   _|      / _|                         | | (_)            
 | |    | |__   ___  ___| | ___ _ __   __ _  | |__  __  _| |_ ___ _ __ _ __   __ _| |   | | | |__) |   | |  _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __  
 | |    | '_ \ / _ \/ __| |/ / | '_ \ / _` | |  __| \ \/ / __/ _ \ '__| '_ \ / _` | |   | | |  ___/    | | | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 | |____| | | |  __/ (__|   <| | | | | (_| | | |____ >  <| ||  __/ |  | | | | (_| | |  _| |_| |       _| |_| | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | |
  \_____|_| |_|\___|\___|_|\_\_|_| |_|\__, | |______/_/\_\\__\___|_|  |_| |_|\__,_|_| |_____|_|      |_____|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|
                                       __/ |                                                                                                                      
                                      |___/                                                                                                                       
                                                             
                                               
''' + RESET)

url = "https://ipinfo.io/json"

resp = urlopen(url)
data = json.load(resp)

ip = data['ip']
city = data['city']
region = data['region']
country = data['country']
loc = data['loc']
org = data['org']
postal = data['postal']
timeZone = data['timezone']

print(BLUE + "OSINT de IP Externo\n" + RESET)
print("IP: {0}\nPaís: {1}\nRegião: {2}\nCidade: {3}\nCEP inicial: {4}\nFuso horário: {5}\nLocalização: {6}\nProvedor de Internet: {7}".format(ip, country, region, city, postal, timeZone, loc, org))