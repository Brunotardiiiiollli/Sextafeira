import tkinter as tk
from PIL import Image, ImageTk
import subprocess

from playsound import playsound

def iniciar_jarvis():
    playsound("áudio/voz_jarvis.mp3")  # toca o áudio de boas-vindas
    subprocess.Popen(["python", "jarvis_core.py"])


# Criação da janela
janela = tk.Tk()
janela.title("Jarvis - Assistente de Voz")
janela.geometry("500x700")
janela.configure(bg="#0f0f0f")

# Carregar imagem do Jarvis (adicione o arquivo jarvis_ui.png ao repositório)
try:
    imagem = Image.open("jarvis_ui.png")
    imagem = imagem.resize((460, 320))
    imagem_tk = ImageTk.PhotoImage(imagem)
    painel = tk.Label(janela, image=imagem_tk, bg="#0f0f0f")
    painel.pack(pady=20)
except:
    pass

# Título
titulo = tk.Label(
    janela,
    text="JARVIS ONLINE",
    font=("Consolas", 24, "bold"),
    fg="#00ffe4",
    bg="#0f0f0f"
)
titulo.pack(pady=10)

# Botão de ativação
botao = tk.Button(
    janela,
    text="Ativar Assistente",
    command=iniciar_jarvis,
    font=("Consolas", 16),
    bg="#00ffe4",
    fg="#0f0f0f",
    padx=20,
    pady=10
)
botao.pack(pady=30)

# Rodapé
rodape = tk.Label(
    janela,
    text="Assistente pessoal de voz",
    font=("Consolas", 10),
    fg="#aaaaaa",
    bg="#0f0f0f"
)
rodape.pack(side="bottom", pady=20)

janela.mainloop()

import subprocess

# Executa o jarvis_core.py ao abrir a interface
subprocess.Popen(["python", "jarvis_core.py"])
