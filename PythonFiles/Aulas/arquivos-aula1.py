# # Arquivos
# from tkinter import *
# from tkinter import filedialog
#
# class Tela:
#     def __init__(self):
#         self.janela_principal = Tk()
#
#         self.barraMenu = Menu(self.janela_principal)
#
#         self.janela_principal.config(menu=self.barraMenu)
#
#         self.barraMenu.add_command(label='Ler arquivo', command=self.lerArquivo)
#
#         mainloop()
#
#     def lerArquivo(self):
#         caminho = filedialog.askopenfile(mode='r', initialdir='D:/Kuro Premium/Downloads', title='Selecione um arquivo', filetypes=[('Arquivo de texto', '*.txt')])  # ou * para todos
#
#         if caminho:
#             conteudo = caminho.read()
#             print(conteudo)
#         else:
#             print('Por favor, escolha um arquivo')
#
#
# interface = Tela()


# # Arquivos2
# from tkinter import *
# from tkinter import filedialog
# from tkinter import scrolledtext
#
# class Tela:
#     def __init__(self):
#         self.janela_principal = Tk()
#
#         self.barraMenu = Menu(self.janela_principal)
#
#         self.janela_principal.config(menu=self.barraMenu)
#
#         self.barraMenu.add_command(label='Ler arquivo', command=self.lerArquivo)
#
#         self.areaTexto = scrolledtext.ScrolledText(self.janela_principal)
#         self.areaTexto.pack(expand=True, fill=BOTH)
#
#         mainloop()
#
#     def lerArquivo(self):
#         caminho = filedialog.askopenfile(mode='r', initialdir='D:/Kuro Premium/Downloads', title='Selecione um arquivo', filetypes=[('Arquivo de texto', '*.py')])  # ou * para todos
#
#         if caminho:
#             conteudo = caminho.read()
#
#             self.areaTexto.insert(INSERT, conteudo)
#         else:
#             print('Por favor, escolha um arquivo')
#
#
# interface = Tela()


# arquivo 3
from tkinter import *
from tkinter import filedialog

class Tela:
    def __init__(self):
        self.janela_principal = Tk()

        self.arquivoAberto = None

        self.criaWidgets()

        mainloop()

    def criaWidgets(self):
        self.labelNome = Label(self.janela_principal, text='Digite o nome do contato:', font=('Arial', '12'))
        self.entryNome = Entry(self.janela_principal, font=('Arial', '12'))

        self.labelTelefone = Label(self.janela_principal, text='Digite o número do contato:', font=('Arial', '12'))
        self.entryTelefone = Entry(self.janela_principal, font=('Arial', '12'))

        self.labelEmail = Label(self.janela_principal, text='Digite o email do contato:', font=('Arial', '12'))
        self.entryEmail = Entry(self.janela_principal, font=('Arial', '12'))

        self.cadastra = Button(self.janela_principal, text='Cadastrar', command=self.salvar)

        self.labelNome.grid(column=0, pady=5)
        self.entryNome.grid(column=1, row=0, pady=5)

        self.labelTelefone.grid(column=0, row=1)
        self.entryTelefone.grid(column=1, row=1)

        self.labelEmail.grid(column=0, row=2)
        self.entryEmail.grid(column=1, row=2, pady=5)

        self.cadastra.grid(column=0, columnspan=2, pady=5)


    def salvar(self):
        nome = self.entryNome.get()
        telefone = self.entryTelefone.get()
        email = self.entryEmail.get()

        if self.arquivoAberto is None:
            self.arquivoAberto = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Arquivos de texto', '*.txt'), (('Todos os arquivos', '*.*'))])

        if self.arquivoAberto is not None:
            dados = open(self.arquivoAberto, 'a')

            dados.write(f'\n\nNome: {nome}\n---->Telefone: {telefone}\n---->Email: {email}')
            dados.close()

        else:
            print('erro')


interface = Tela()