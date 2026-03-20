import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulario de Cadastro")
janela.geometry("800x500")


def enviar():
    nome = entrada_nome.get()
    sobrenome = ent_sobrenome.get()
    data_de_nascimento = data_nasc.get()
    cpf = ent_cpf.get()
    cep = ent_cep.get()
    sexo = ent_sexo.get()
    estado = ent_estado.get()
    cidade = ent_cidade.get()

    sexo_texto = "Masculino" if sexo == 1 else "Feminino"
   

    msg = f"Nome: {nome}\n Sobrenome: {sobrenome}\n Data de Nascimento: {data_de_nascimento}\n CPF: {cpf}\n CEP: {cep}\n Sexo: {sexo_texto}\n Estado: {estado}\n Cidade: {cidade}"
    messagebox.showinfo("Cadastrado", msg)



tk.Label(janela, text="Formulário de Cadastro", font=("Arial",14)).grid(column=1, pady=20)


tk.Label(janela, text="Nome:",  font=("Arial")).grid(row=2, column=0)
entrada_nome= tk.Entry(janela,font=("Papyrus"))
entrada_nome.grid(row=2, column=1)

tk.Label(janela, text="Sobrenome:",  font=("Arial")).grid(row=3, column=0, pady=8)
ent_sobrenome= tk.Entry(janela,font=("Papyrus"))
ent_sobrenome.grid(row=3, column=1)

tk.Label(janela, text="Data de Nascimento:", font=("Arial")).grid(row=4, column=0, pady=10)
data_nasc = tk.Entry(janela, font=("Papyrus"))
data_nasc.grid(row=4, column=1)

tk.Label(janela, text="CPF:", font=("Arial")).grid(row=5, column=0, pady=10)
ent_cpf = tk.Entry(janela, font=("Papyrus"))
ent_cpf.grid(row=5, column=1)

tk.Label(janela, text="CEP:", font=("Arial")).grid(row=6, column=0, pady=10)
ent_cep = tk.Entry(janela, font=("Papyrus"))
ent_cep.grid(row=6, column=1)



tk.Label(janela, text="Estado:", font=("Arial")).grid(row=11, column=0, pady=10)
ent_estado = ttk.Combobox(janela, font=("Papyrus"),values=["MG", "SP", "RJ", "BA", "RN"])
ent_estado.grid(row=11, column=1)

tk.Label(janela, text="Cidade:", font=("Arial")).grid(row=12, column=0, pady=10)
ent_cidade = tk.Entry(janela, font=("Papyrus"))
ent_cidade.grid(row=12, column=1)




ent_sexo = tk.IntVar()
tk.Label(janela, text="Sexo:", font=("Arial")).grid(row=7, column=0, pady=10)
tk.Radiobutton(janela, text="Masculino", font=("Papyrus") ,value=1, variable=ent_sexo)\
    .grid(row=7, column=1)
tk.Radiobutton(janela, text="Feminino", font=("Papyrus") ,value=2, variable=ent_sexo)\
    .grid(row=8, column=1)




tk.Button(janela, text="Enviar", command=enviar).grid(row=19, column=1, pady=20)


janela.mainloop()