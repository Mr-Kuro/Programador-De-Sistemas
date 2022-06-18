from usuarios import Usuarios
from tkinter import *


class Application:

    def __init__(self):
        self.janela_principal = Tk()

        self.fonte = ('verdana', '8')

        self.container1 = Frame(self.janela_principal, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.janela_principal, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.janela_principal, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.janela_principal, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(self.janela_principal, padx=20, pady=5)
        self.container5.pack()

        self.container6 = Frame(self.janela_principal, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.janela_principal, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.janela_principal, padx=20, pady=5)
        self.container8.pack()

        self.container9 = Frame(self.janela_principal, pady=15)
        self.container9.pack()

        self.titulo = Label(self.container1, text='Informe os dados')
        self.titulo['font'] = ('Calibri', '15', 'bold')
        self.titulo.pack()

        self.labelId = Label(self.container2,
                             text='Id Usuário:',
                             font=self.fonte,
                             width=10)
        self.labelId.pack(side=LEFT)

        self.inputId = Entry(self.container2,
                             width=16,
                             font=self.fonte)
        self.inputId.pack(side=LEFT, padx=8)

        self.buscar = Button(
            self.container2,
            text='Buscar',
            font=self.fonte,
            width=7,
            command=self.buscarUsuario)
        self.buscar.pack(side=RIGHT)

        self.labelNome = Label(
            self.container3,
            text='Nome:',
            font=self.fonte,
            width=10)
        self.labelNome.pack(side=LEFT)

        self.inputNome = Entry(
            self.container3,
            width=25,
            font=self.fonte)
        self.inputNome.pack(side=LEFT, padx=8)

        self.labelTelefone = Label(
            self.container4,
            text='Telefone:',
            width=10,
            font=self.fonte)
        self.labelTelefone.pack(side=LEFT)

        self.inputTelefone = Entry(
            self.container4,
            width=25,
            font=self.fonte)
        self.inputTelefone.pack(side=LEFT, padx=7)

        self.labelEmail = Label(
            self.container5,
            width=10,
            text='Email:',
            font=self.fonte)
        self.labelEmail.pack(side=LEFT)

        self.inputEmail = Entry(
            self.container5,
            width=25,
            font=self.fonte)
        self.inputEmail.pack(side=LEFT, padx=11)

        self.labelUsuario = Label(
            self.container6,
            width=10,
            text='Usuário',
            font=self.fonte)
        self.labelUsuario.pack(side=LEFT)

        self.inputUsuario = Entry(
            self.container6,
            width=25,
            font=self.fonte)
        self.inputUsuario.pack(side=LEFT, padx=8)

        self.labelSenha = Label(
            self.container7,
            width=10,
            text='Senha:',
            font=self.fonte)
        self.labelSenha.pack(side=LEFT)

        self.inputSenha = Entry(
            self.container7,
            width=25,
            font=self.fonte,
            show='*')
        self.inputSenha.pack(side=LEFT, padx=8)

        self.inserir = Button(
            self.container8,
            width=10,
            text='Inserir',
            font=self.fonte,
            command=self.inserirUsuario)
        self.inserir.pack(side=LEFT)

        self.editar = Button(
            self.container8,
            width=10,
            text='Alterar',
            font=self.fonte,
            command=self.alterarUsuario)
        self.editar.pack(side=LEFT, padx=8)

        self.excluir = Button(
            self.container8,
            width=10,
            text='excluir',
            font=self.fonte,
            command=self.excluirUsuario)
        self.excluir.pack(side=LEFT)

        self.mensagem = Label(self.container9, text='',)
        self.mensagem['font'] = ('Verdana', '9', 'italic')
        self.mensagem.pack()

        mainloop()

    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.inputId.get()

        self.mensagem['text'] = user.deleteUser()

        self.inputNome.delete(0, END)
        self.inputTelefone.delete(0, END)
        self.inputEmail.delete(0, END)
        self.inputUsuario.delete(0, END)
        self.inputSenha.delete(0, END)
        self.inputId.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.inputId.get()
        user.nome = self.inputNome.get()
        user.telefone = self.inputTelefone.get()
        user.usuario = self.inputUsuario.get()
        user.email = self.inputEmail.get()
        user.senha = self.inputSenha.get()

        self.mensagem['text'] = user.updateUser()

        self.inputNome.delete(0, END)
        self.inputTelefone.delete(0, END)
        self.inputEmail.delete(0, END)
        self.inputUsuario.delete(0, END)
        self.inputSenha.delete(0, END)
        self.inputId.delete(0, END)

    def inserirUsuario(self):
        user = Usuarios()

        user.nome = self.inputNome.get()
        user.telefone = self.inputTelefone.get()
        user.usuario = self.inputUsuario.get()
        user.email = self.inputEmail.get()
        user.senha = self.inputSenha.get()

        self.mensagem['text'] = user.insertUser()

        self.inputNome.delete(0, END)
        self.inputTelefone.delete(0, END)
        self.inputEmail.delete(0, END)
        self.inputUsuario.delete(0, END)
        self.inputSenha.delete(0, END)
        self.inputId.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.inputId.get()

        self.mensagem['text'] = user.selectUser(idusuario)

        self.inputId.delete(0, END)
        self.inputId.insert(INSERT, user.idusuario)

        self.inputNome.delete(0, END)
        self.inputNome.insert(INSERT, user.nome)

        self.inputTelefone.delete(0, END)
        self.inputTelefone.insert(INSERT, user.telefone)

        self.inputEmail.delete(0, END)
        self.inputEmail.insert(INSERT, user.email)

        self.inputUsuario.delete(0, END)
        self.inputUsuario.insert(INSERT, user.usuario)

        self.inputSenha.delete(0, END)
        self.inputSenha.insert(INSERT, user.senha)


minhaInterface = Application()
