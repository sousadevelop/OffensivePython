## O segredo que todos procuram, mas poucos acham...Você será capaz de desvendar ? ##

from stegano import lsb

# Cores
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

print(CYAN + '''


  _____                      _ _               _    _ _     _     _              _  __              
 |  __ \                    | (_)             | |  | (_)   | |   | |            | |/ /              
 | |__) |_____   _____  __ _| |_ _ __   __ _  | |__| |_  __| | __| | ___ _ __   | ' / ___ _   _ ___ 
 |  _  // _ \ \ / / _ \/ _` | | | '_ \ / _` | |  __  | |/ _` |/ _` |/ _ \ '_ \  |  < / _ \ | | / __|
 | | \ \  __/\ V /  __/ (_| | | | | | | (_| | | |  | | | (_| | (_| |  __/ | | | | . \  __/ |_| \__ \
 |_|  \_\___| \_/ \___|\__,_|_|_|_| |_|\__, | |_|  |_|_|\__,_|\__,_|\___|_| |_| |_|\_\___|\__, |___/
                                        __/ |                                              __/ |    
                                       |___/                                              |___/     

                                                             

                                               
''' + RESET)

# Gerando um arquivo com texto dentro
secret = lsb.hide("./pexels-anton-atanasov-213172.png", "NjNjZjVlMmEyN2E2OWZkOGZmNGRkZmNhYWZlYmRmY2JmOWRjZWVlZg==")
secret.save(r'''C:\Windows\Temp\life_secret.png''')

# Revelando o texto oculto no arquivo
#awake_true = lsb.reveal("C:\Windows\Temp\life_secret.png")
#print(awake_true)