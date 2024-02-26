# Ware Scan 🐍

<p align="left">
	<a href="https://www.python.org/"><img src="https://img.shields.io/badge/made%20with-python-green"></a>
	<a href="https://nmap.org/"><img src="https://img.shields.io/badge/made%20with-nmap-blueviolet"></a>
</p>

- [Resumo](#Resumo)
- [Executando](#Executando)
- [Uso](#Uso)
- [Avisos](#Avisos)

# Resumo
O scanner de portas é uma ferramenta da rede utilizada para realizar uma varredura de serviços em determinado IP ou Host. A ferramenta Nmap é a mais conhecida, por seus scanners personalizados e foco em vulnerabilidades. Aqui você encontrará três ferramentas que realizam a mesma coisa, mas caberá a você escolher a que mais se encaixa no seu contexto. Duas delas são integradas com o Nmap, a outra é mais simples utilizando apenas o socket.

# Executando

Executando o warescan.py:
![warescan](img/image.png)

Executando o warescan_nmap.py:
![warescan_nmap](img/image-1.png)

Executando o warescan_nmap_graphic.py:
![warescan_nmap_graphic](img/image-2.png)

# Uso 

Você pode usar no terminal o warescan.py:
```sh
python3 warescan.py
```
Ou o warescan_nmap.py:
```sh
python3 warescan_nmap.py
```
Ou o warescan_nmap_graphic.py:

# Avisos

Caso você esteja usando o Windows e queira usar uma ferramenta com Nmap, siga os passos abaixo:

1. Instale o Nmap -> https://nmap.org/download#windows
2. Instale o Npcap -> https://npcap.com/#download

Lembre-se de configurar o nmap nas suas variáveis de ambiente!

Contudo, caso esteja usando o Linux, você precisa estar executar os programas com o usuário root. Para isso use no terminal que for usar para executar os programas:

- sudo su
```sh
python3 warescan_nmap_graphic.py
```

Todos possuem uma interface objetiva e de fácil compreensão, por isso não irei detalhar o uso interno, pois já fiz isso no código.
