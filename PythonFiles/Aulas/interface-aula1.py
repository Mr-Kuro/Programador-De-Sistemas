from tkinter import *
janela = Tk()
# importar o framework de interface)
# criar janela
label1 = Label(
    text='Hello World',
    foreground='white',  # texto branco
    background='black'  # fundo preto
)
label1.pack()
janela.mainloop()


# from tkinter import *
# janela = Tk()
# label1 = Label(text='Bankai')
# label2 = Label(
#     text='Hello Universe',
#     background='#34A3FE'  # essa cor é azul claro
# )
# # criar texto
# label1.pack()
# label2.pack()
# # colocar texto na janela
# janela.mainloop()
# # ele diz ao python pra executar o loop de eventos do tkinter


# from tkinter import *
# janela = Tk()
# label1 = Label(
#     text='Helo World',
#     fg='white',
#     bg='black',
#     width=50,
#     height=20
# )
# label1.pack()
# janela.mainloop()


# from tkinter import *
# janela = Tk()
# botao = Button(
#     text='Click me',
#     width=25,
#     height=10,
#     bg='blue',
#     fg='yellow'
# )
# botao.pack()
# janela.mainloop()


# from tkinter import *
# janela = Tk()
#
# entrada = Entry(
#     fg='yellow', bg='blue',
#     width=50,  # tamanho de 50 caracteres
# )
#
# entrada.pack()
# janela.mainloop()


# import tkinter as tk
# janela = tk.Tk()
# label = tk.Label(text='nome')
# label.pack()
# entry = tk.Entry()
# entry.pack()
# nome = entry.get()
# print(nome)
# entry.delete(0, tk.END)  # 0 até o fim
# print(nome)
# entry.insert(0, 'Luana')
# janela.mainloop()

# window = Tk()
# texto1 = Text()
# texto1.pack()
# nome = texto1.get(1.0)
# print(nome)
# nome = texto1.get(1.0, 1.5)
# print(nome)
# texto1.delete(1.0)
# texto1.delete(1.0, 1.4)
# texto1.delete(1.0, END)  # do inicio ao fim
# texto1.insert(1.0, 'hello')
# texto1.insert(2.0, '\nWorld')
# texto1.insert(END, 'final')
# window.mainloop()
