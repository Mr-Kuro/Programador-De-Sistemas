# from tkinter import *
#
# class Interface:
#     def __init__(self):
#         self.janela_principal = Tk()
#
#         self.fontePadrao = ('arial', '10')
#
#         # criando primeiro container
#         self.primeiroContainer = Frame(
#             self.janela_principal,
#             pady=10
#         )
#         self.primeiroContainer.pack()
#
#         # criando segundo container
#         self.segundoContainer = Frame(
#             self.janela_principal,
#             padx=20
#         )
#         self.segundoContainer.pack()
#
#         # criando terceiro container
#         self.terceiroCopntainer = Frame(
#             self.janela_principal,
#             padx=20
#         )
#         self.terceiroCopntainer.pack()
#
#         # quarto container
#         self.quartoContainer = Frame(self.janela_principal, pady=20)
#         self.quartoContainer.pack()
#
#         # criando Título do sistema
#         self.titulo = Label(self.primeiroContainer, text='Dados do usuario')
#         self.titulo['font'] = ('Arial', '10', 'bold')
#         self.titulo.pack()
#
#         # criando label de nome
#         self.nomeLabel = Label(self.segundoContainer, text='Nome', font=self.fontePadrao)
#         self.nomeLabel.pack(side='left')
#
#         # criando caixa de texto de nome
#         self.nome = Entry(self.segundoContainer, width=30, font=self.fontePadrao)
#         self.nome.pack(side='left')
#
#         # criando label de senha
#         self.senhaLabel = Label(self.terceiroCopntainer, text='Senha', font=self.fontePadrao)
#         self.senhaLabel.pack(side=LEFT)
#
#         # criando caixa de texto de senha
#         self.senha = Entry(self.terceiroCopntainer, width=30, font=self.fontePadrao, show='*')
#         self.senha.pack(side=LEFT)
#
#         # criando botao de autenticar
#         self.autenticar = Button(self.quartoContainer, text='Autenticar', command=self.verificaSenha)
#         self.autenticar['font'] = ('Calibre', '8')
#         self.autenticar.pack()
#
#         # informar se a autenticação foi válida ou não (confirmação do login)
#         self.mensagem = Label(self.quartoContainer, '', font=self.fontePadrao)
#         self.mensagem.pack()
#
#         mainloop()
#
#     #      método que verifica as informações digitadas
#     def verificaSenha(self):
#         usuario = self.nome.get()
#         senha = self.senha.get()
#         if usuario == 'Ícaro' and senha == 'dev123':
#             self.mensagem['text'] = 'Autenticado.'
#         else:
#             self.mensagem['text'] = 'Erro na autenticação.'
#
#
# # teste da class
#
# home = Interface()
#
from tkinter import *
from tkinter import messagebox

class Interface:
    def __init__(self):
        self.janela_principal = Tk()

        # criando os frames
        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)

        self.frame_cima.pack()
        self.frame_baixo.pack()

        # objeto intvar dos botoes
        self.radio_valor = IntVar()
        self.radio_valor.set(2)  # primeira opção marcada inialmente

        self.label = Label(self.frame_cima, text='Qual a sua linguagem de programação preferida?')
        self.python = Radiobutton(self.frame_cima, text='Python', variable=self.radio_valor, value=1, command=self.exibe)
        self.java = Radiobutton(self.frame_cima, text='Java', variable=self.radio_valor, value=2, command=self.exibe)
        self.c = Radiobutton(self.frame_cima, text='c', variable=self.radio_valor, value=3, command=self.exibe)

        self.label.pack(anchor='w')
        self.python.pack(anchor='w')
        self.java.pack(anchor='w')
        self.c.pack(anchor='w')

        self.sair = Button(self.frame_baixo, text='Sair', command=self.janela_principal.destroy)
        self.sair.pack()

        mainloop()

    def exibe(self):
        nome = str(self.radio_valor.get())
        messagebox.showinfo('Resposta', f'você escolheu a opção {nome}')





# from tkinter import *
#
# from tkinter import messagebox
#
#
# class Interface:
#     def __init__(self):
#         self.texto = ''
#         self.janela_principal = Tk()
#
#         # criando os frames
#         self.frame_cima = Frame(self.janela_principal)
#         self.frame_baixo = Frame(self.janela_principal)
#
#         self.frame_cima.pack()
#         self.frame_baixo.pack()
#
#         # objeto intvar dos botoes
#         self.checkVar1 = IntVar()
#         self.checkVar2 = IntVar()
#         self.checkVar3 = IntVar()
#         self.checkVar4 = IntVar()
#
#         # Setando zero para aparecerem desmarcados
#         self.checkVar1.set(0)
#         self.checkVar2.set(0)
#         self.checkVar3.set(0)
#         self.checkVar4.set(0)
#
#         self.label = Label(self.frame_cima, text='Que gêneros(s) musical(is) você gosta?')
#         self.check1 = Checkbutton(self.frame_cima, text='Rock', variable=self.checkVar1)
#         self.check2 = Checkbutton(self.frame_cima, text='Gospel', variable=self.checkVar2)
#         self.check3 = Checkbutton(self.frame_cima, text='Funk', variable=self.checkVar3)
#         self.check4 = Checkbutton(self.frame_cima, text='Pop', variable=self.checkVar4)
#
#         # pack Radiobuttons
#         self.label.pack(anchor='w')
#         self.check1.pack(anchor='w')
#         self.check2.pack(anchor='w')
#         self.check3.pack(anchor='w')
#         self.check4.pack(anchor='w')
#
#         # botão de sair
#         self.botao = Button(self.frame_baixo, text='Exibir escolha', command=self.exibe)
#         self.sair = Button(self.frame_baixo, text='Sair', command=self.janela_principal.destroy)
#         self.botao.pack(side=LEFT)
#         self.sair.pack(side=LEFT)
#
#         mainloop()
#
#     def exibe(self):
#         self.texto = 'você curte: \n'
#         if self.checkVar1.get() == 1:
#             self.texto += 'Rock\n'
#         if self.checkVar2.get() == 1:
#             self.texto += 'Gospel\n'
#         if self.checkVar3.get() == 1:
#             self.texto += 'Funk\n'
#         if self.checkVar4.get() == 1:
#             self.texto += 'Pop\n'
#         messagebox.showinfo(f'Seu gosto musical:', self.texto)


# teste da class
minhainterface = Interface()
