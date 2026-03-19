import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulario")
janela.geometry("300x300")


def enviar():
    nome = entrada_nome.get()
    idade = ler_idade.get()
    escolaridade = combo_escola.get()
    area_de_atuacao = opc.get()

    if opc.get() == 1:
        area_de_atuacao = "Técnico em Informática"
    elif opc.get() == 2:
        area_de_atuacao = "Administração"
    elif opc.get() == 3:
        area_de_atuacao = "Engenharia"
    elif opc.get() == 4:
        area_de_atuacao = "Marketing"
   

    msg = f"Nome: {nome}\n Idade: {idade}\n Escolaridade: {escolaridade}\n Área de Atuação: {area_de_atuacao}"
    messagebox.showinfo("Dados Enviados", msg)



tk.Label(janela, text="Formulário de Cadastro", font=("Arial",14)).grid(column=1, pady=20)
tk.Label(janela, text="Dados Pessoais", font=("Arial",14)).grid(column=1, pady=20)
tk.Label(janela, text="Dados Profissionais", font=("Arial",14)).grid(row=8, column=1, pady=20)

tk.Label(janela, text="Nome:",  font=("Arial")).grid(row=2, column=0)
entrada_nome= tk.Entry(janela,font=("Papyrus"))
entrada_nome.grid(row=2, column=1)

tk.Label(janela, text="Idade:",  font=("Arial")).grid(row=3, column=0, pady=8)
ler_idade= tk.Entry(janela,font=("Papyrus"))
ler_idade.grid(row=3, column=1)



tk.Label(janela, text="Escolaridade:", font=("Arial")).grid(row=10, column=0, pady=10)
combo_escola = ttk.Combobox(janela, values=["Ensino Fundamental Completo", "Ensino Médio Completo", "Ensino Superior", "Pós-Graduação"])
combo_escola.grid(row=10, column=1)


opc = tk.IntVar()
tk.Label(janela, text="Área de Atuação:", font=("Arial")).grid(row=13, column=0)
opc1 = tk.Radiobutton(janela, value=1,text="Técnico em Informática", font=("Papyrus") , variable=opc)\
    .grid(row=13, column=1)
opc2 = tk.Radiobutton(janela, value=2,text="Administração", font=("Papyrus") , variable=opc)\
    .grid(row=14, column=1)
opc3 = tk.Radiobutton(janela, value=3,text="Engenharia", font=("Papyrus") , variable=opc)\
    .grid(row=15, column=1)
opc4 = tk.Radiobutton(janela, value=4,text="Marketing", font=("Papyrus") , variable=opc)\
    .grid(row=16, column=1)



tk.Button(janela, text="Enviar", command=enviar).grid(row=19, column=1, pady=20)


janela.mainloop()