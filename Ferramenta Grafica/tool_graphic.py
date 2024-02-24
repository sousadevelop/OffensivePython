import webbrowser
from tkinter import *

# Display do Programa
root = Tk( )

# Título do programa
root.title("Estudos de Hacker")
# Tamanho inicial da tela
root.geometry("400x400")

def hacktricks():
    webbrowser.open("https://book.hacktricks.xyz/welcome/readme")

def tryhackme():
    webbrowser.open("https://tryhackme.com/dashboard")

def solyd():
    webbrowser.open("https://www.youtube.com/playlist?list=PLp95aw034Wn8Wi0NViVF58hOpX-m00jyg")

def jotbot():
    webbrowser.open("https://app.myjotbot.com/")

def owasp_web():
    webbrowser.open("https://owasp.org/www-project-web-security-testing-guide/latest/")

# Cria botões                                           chama a função       tamanho do botão
B_hacktricks = Button(root, text="Abrir o HackTricks", command=hacktricks). pack(pady=20)
B_tryhackme = Button(root, text="Abrir o TryHackMe", command=tryhackme). pack(pady=20)
B_solyd = Button(root, text="Abrir o Curso da Solyd", command=solyd). pack(pady=20)
B_jotbot = Button(root, text="Abrir o JotBot", command=jotbot). pack(pady=20)
B_owap_web = Button(root, text="Abrir o Owasp Web", command=owasp_web). pack(pady=20)

# Executa o programa
root.mainloop()