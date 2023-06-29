import tkinter as tk
from pyqrcode import QRCode

def generate_qr_code():
    link = entry.get()
    qr = QRCode(link)
    qr.png('qrcode.png', scale=5)

    # Atualizando a imagem exibida na interface gráfica
    img = tk.PhotoImage(file="qrcode.png")
    qr_label.config(image=img)
    qr_label.image = img

# Criação da janela principal
window = tk.Tk()
window.title("Gerador de QR Code")

# Campo de entrada para o link
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Botão para gerar o QR Code
generate_button = tk.Button(window, text="Gerar QR Code", command=generate_qr_code)
generate_button.pack(pady=5)

# Rótulo para exibir o QR Code gerado
qr_label = tk.Label(window)
qr_label.pack()

# Execução da interface gráfica
window.mainloop()
