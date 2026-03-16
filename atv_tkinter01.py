import tkinter as tk

janela_main = tk.Tk()

janela_main.title("Gorillaz")
janela_main.configure(background="green")
janela_main.minsize(200,200)
#janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#OBJETOS M JANELA
tk.Label(janela_main,
         text="Gorillaz The Mountain",
         bg="green",
         font=("Papyrus",20, "bold"),
         ).pack()

imagem = tk.PhotoImage(file="gorillaz2.png")
imagem = imagem.subsample(1,1)
tk.Label(janela_main, image=imagem).pack()

tk.Label(janela_main,
         text="Álbum lançado recentemente",
         bg="green",
         font=("Arial",20, ),
         ).pack()


janela_main.mainloop()