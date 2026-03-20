import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Conectar")
janela.configure(background="Gray")

def enviar():
    nome = entrada_nome.get()
    senha = ler_senha.get()

    msg = "Usuário logado com sucesso"
    messagebox.showinfo("LOGADO!", msg)


tk.Label(janela, text="Fazer Login", font=("Arial",14)).grid(column=1, pady=20)


tk.Label(janela, text="Usuário:",  font=("Arial")).grid(row=2, column=0, pady=8)
entrada_nome= tk.Entry(janela,font=("Papyrus"))
entrada_nome.grid(row=2, column=1)

tk.Label(janela, text="Senha:",  font=("Arial")).grid(row=3, column=0, pady=8)
ler_senha= tk.Entry(janela,font=("Papyrus"))
ler_senha.grid(row=3, column=1)

imagem = tk.PhotoImage(file="download.png")
imagem = imagem.subsample(1,1)
tk.Label(janela,image=imagem).grid(row=2, column=20)

tk.Button(janela, text="Enviar", command=enviar).grid(row=7, column=0, pady=20)




janela.mainloop()