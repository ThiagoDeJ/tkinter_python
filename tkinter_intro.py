import tkinter as tk
#Criação de janela
janela_main = tk.Tk()

janela_main.title("Red Dead Redemption")
janela_main.configure(background="red")
janela_main.minsize(200,200)
#janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#OBJETOS M JANELA
tk.Label(janela_main,
         text="Hello World",
         bg="red",
         font=("Papyrus",20, "bold"),
         ).pack()
tk.Label(janela_main,
         text="Thiago de Jesus",
         bg="red",
         font=("Papyrus",20, ),
         ).pack()
#imagens
imagem = tk.PhotoImage(file="life.png")
imagem = imagem.zoom(2,2)
tk.Label(janela_main, image=imagem).pack()


janela_main.mainloop()