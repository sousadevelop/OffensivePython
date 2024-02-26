import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import nmap

class WareScanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("WareScan With Nmap")
        self.create_widgets()

    def create_widgets(self):
        # Carregar a imagem
        img_path = "img/jeremy-bishop-G9i_plbfDgk-unsplash.jpg"
        original_img = Image.open(img_path)

        # Redimensionar a imagem para o tamanho da janela
        width, height = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        resized_img = original_img.resize((width, height))
        img = ImageTk.PhotoImage(resized_img)

        # Criar um rótulo com a imagem como plano de fundo
        background_label = tk.Label(self.master, image=img)
        background_label.image = img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Configurar o tamanho inicial da janela
        width, height = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry(f"{width//2}x{height//2}+{width//4}+{height//4}")

        # Labels
        self.label_ip = ttk.Label(self.master, text="Digite o IP ou Host que deseja scannear:")
        self.label_ip.pack(pady=(height//6, 5))

        self.entry_ip = ttk.Entry(self.master, width=30)
        self.entry_ip.pack(pady=5)

        self.label_varredura = ttk.Label(self.master, text="Escolha o tipo de varredura:")
        self.label_varredura.pack(pady=5)

        self.combo_varredura = ttk.Combobox(self.master, values=["SYN", "UDP", "TCP Intenso"])
        self.combo_varredura.pack(pady=5)

        self.button_scan = ttk.Button(self.master, text="Iniciar Varredura", command=self.iniciar_varredura, style='TButton')
        self.button_scan.pack(pady=10)

        style = ttk.Style()
        style.configure('TButton', foreground='black', background='#274472', font=('Nunito', 12))

        self.label_resultado = ttk.Label(self.master, text="")
        self.label_resultado.pack(pady=5)

    def iniciar_varredura(self):
        ip = self.entry_ip.get()
        varredura = self.combo_varredura.get()

        if not ip or not varredura:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        scanner = nmap.PortScanner()
        try:
            if varredura == "SYN":
                scanner.scan(ip, '1-1024', '-v -sS')
            elif varredura == "UDP":
                scanner.scan(ip, '1-1024', '-v -sU')
            elif varredura == "TCP Intenso":
                scanner.scan(ip, '1-1024', '-v -sC')
            else:
                messagebox.showerror("Erro", "Tipo de varredura inválido.")
                return

            resultado = f"Versão do Nmap: {scanner.nmap_version()}\n"
            resultado += f"Status do IP: {scanner[ip].state()}\n"
            resultado += f"Todos os protocolos: {scanner[ip].all_protocols()}\n\n"

            if varredura == "UDP" and 'udp' in scanner[ip].all_protocols():
                resultado += f"Portas Abertas (UDP): {scanner[ip]['udp'].keys()}\n"
            else:
                resultado += f"Portas Abertas: {scanner[ip]['tcp'].keys()}\n"

            self.label_resultado.config(text=resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a varredura: {str(e)}")

# Criar a janela principal
root = tk.Tk()
app = WareScanGUI(root)

# Iniciar o loop principal da interface gráfica
root.mainloop()
