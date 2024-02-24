import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
import pyperclip

# Função para calcular o hash
def calcular_hash():
    texto = entry_texto.get()
    tipo_hash = combo_tipo_hash.get()

    if tipo_hash == "MD5":
        resultado = hashlib.md5(texto.encode("utf-8")).hexdigest()
    elif tipo_hash == "SHA1":
        resultado = hashlib.sha1(texto.encode("utf-8")).hexdigest()
    elif tipo_hash == "SHA224":
        resultado = hashlib.sha224(texto.encode("utf-8")).hexdigest()
    elif tipo_hash == "SHA256":
        resultado = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    elif tipo_hash == "SHA512":
        resultado = hashlib.sha512(texto.encode("utf-8")).hexdigest()
    else:
        messagebox.showerror("Erro", "Tipo de hash inválido")
        return

    label_resultado.config(text=f"O hash {tipo_hash} da string é -> {resultado}")
    button_copiar.config(state=tk.NORMAL)  # Habilitar o botão de copiar

# Função para copiar o texto para a área de transferência
def copiar_texto():
    texto = label_resultado.cget("text")
    texto = texto.split("->")[1].strip()
    pyperclip.copy(texto)
    messagebox.showinfo("Copiado", "Texto copiado para a área de transferência!")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Hash")

# Criar e adicionar widgets
label_titulo = tk.Label(root, text="Calculadora de Hash", font=("Helvetica", 16, "bold"))
label_titulo.pack(pady=10)

label_texto = tk.Label(root, text="Digite o texto:")
label_texto.pack()

entry_texto = tk.Entry(root, width=50)
entry_texto.pack(pady=10)

label_tipo_hash = tk.Label(root, text="Escolha o tipo de hash:")
label_tipo_hash.pack()

tipos_hash = ["MD5", "SHA1", "SHA224", "SHA256", "SHA512"]
combo_tipo_hash = ttk.Combobox(root, values=tipos_hash)
combo_tipo_hash.pack(pady=10)

button_calcular = tk.Button(root, text="Calcular Hash", command=calcular_hash)
button_calcular.pack(pady=10)

label_resultado = tk.Label(root, text="")
label_resultado.pack()

button_copiar = tk.Button(root, text="Copiar", command=copiar_texto, state=tk.DISABLED)
button_copiar.pack(pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
