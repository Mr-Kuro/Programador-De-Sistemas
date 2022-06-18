# from tkinter import messagebox

# mostrando informação

# messagebox.showinfo('Mostrando informação', 'informação aqui')
# # o atributo 1 é o título, o atributo 2 é a informação

# messagebox.showwarning('Mostrando alerta', 'Alerta aqui')
# # o atributo 1 é o título, o atributo 2 é a informação

# messagebox.showerror('Mostrando erro', 'Erro aqui')
# # o atributo 1 é o título, o atributo 2 é a informação


# perguntando ao usuário

# messagebox.askquestion('Mostrar pergunta', 'pergunta aqui')
# # o atributo 1 é o título, o atributo 2 é a informação

# messagebox.askokcancel('Mostrar pergunta', 'pergunta aqui')
# # o atributo 1 é o título, o atributo 2 é a informação

# messagebox.askyesno('Mostrar pergunta', 'pergunta aqui')
# # # o atributo 1 é o título, o atributo 2 é a informação
#
# messagebox.askretrycancel('Mostrar pergunta', 'pergunta aqui')
# # # o atributo 1 é o título, o atributo 2 é a informação
# # # repetir, cancelar

# from tkinter import *

# class Interface:
#     def __init__(self):
#         # criando a janela principal
#         self.janelaPrincipal = Tk()
#
#         self.menssagem = Label(
#             master=self.janelaPrincipal,
#             text='Primeiro widget usando POO',
#         )
#         self.menssagem['font'] = ('verdana', '12', 'italic', 'bold')
#         # modificar a fonte da Label
#
#         self.menssagem.pack()
#         self.sair = Button(self.janelaPrincipal)
#         self.sair["text"] = 'sair'
#         self.sair['font'] = ('calibri', '10')
#         self.sair['command'] = self.janelaPrincipal.destroy  # no lugar de destroy quit para apenas parar
#         self.sair.pack()
#
#         mainloop()


# from tkinter import messagebox
#
# class Interface:
#     def __init__(self):
#         # criando a janela principal
#         self.janelaPrincipal = Tk()
#
#         #criando botão
#         self.botao = Button(self.janelaPrincipal, text='Clique-me', command=self.helle_world)
#         self.botao['font'] = ('calibri', '10')
#         self.botao.pack()
#
#         #criando botão
#         self.sair = Button(self.janelaPrincipal, text='sair2', command=self.janelaPrincipal.destroy)
#         self.sair.pack()
#
#         mainloop()
#
#     def helle_world(self):
#         messagebox.showinfo('Hello, World')


from tkinter import *

class Interface:
    def __init__(self):
        self.janela_principal = Tk()

        self.msg = Label(self.janela_principal, text='Primeiro widget')
        self.msg['font'] = ('calibri', '25', 'italic')
        self.msg.pack()

        self.botao = Button(self.janela_principal, text='Clique aqui', width=10, command=self.mudarTexto)
        self.botao['font'] = ('calibri', '25')
        self.botao.pack()

        mainloop()

    def mudarTexto(self):
        if self.msg['text'] == 'primeiro widget':
            self.msg['text'] = 'o botão recebeu um clique'
        else:
            self.msg['text'] = 'primeiro widget'


# from tkinter import *
#
# class Interface:
#     def __init__(self):
#         self.janela_principal = Tk()
#
#         self.frame_cima = Frame(self.janela_principal)
#         self.frame_meio = Frame(self.janela_principal)
#         self.frame_baixo = Frame(self.janela_principal)
#
#         self.msg = Label(self.frame_cima, text='Digite seu nome:')
#         self.msg.pack(side='left')
#
#         self.entrada = Entry(self.frame_cima, width=30)
#         self.entrada.pack(side='left')
#
#         self.label = Label(self.frame_meio, text='Seu nome é: ')
#         self.label.pack(side='left')
#         self.labelDinamica = StringVar()
#         self.label2 = Label(self.frame_meio, textvariable=self.labelDinamica)
#         self.label2.pack(side='left')
#
#         self.botao = Button(self.frame_baixo, text='Exibir', command=self.exibe)
#         self.sair = Button(self.frame_baixo, text='Sair', command=self.janela_principal.destroy)
#         self.botao.pack(side='left')
#         self.sair.pack(side='left')
#
#         self.frame_cima.pack()
#         self.frame_meio.pack()
#         self.frame_baixo.pack()
#
#         mainloop()
#
#     def exibe(self):
#         nome = self.entrada.get()
#         self.labelDinamica.set(nome)


# Teste da classe
minhainterface = Interface()
