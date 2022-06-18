import sqlite3
from tkinter import *

# INSERIR, UPDADE BUSCAR, DELETAR, LER = CUOD


# cria a conexão com o banco de dados
conn = sqlite3.connect("database.db")

# o cursor é mais seguroque:
# cria a tabela de administrador do sistema
conn.execute("""
CREATE TABLE IF NOT EXISTS admin(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
username Text NOT NULL,
password TEXT NOT NULL)
              """)

# inserindo dados na tabela
conn.execute("INSERT INTO admin(username, password) VALUES('Anderson', '9850')")
conn.execute("INSERT INTO admin(username, password) VALUES('admin', 'admin.9')")

# persistindo o que foi dito a cima
conn.commit()

# fechando a conexão
conn.close()


def login():
    # criando variáveis para armazenar o que incrementado pelo usuario
    uname = username.get()
    pwd = password.get()

    # verificando se alguns dos campos está vazio
    if uname == '' or pwd == '':
        # se estiver: presso que o usuario preencha
        message.set('Preencha os campos que estão vazios!!!')
    else:
        # abro uma nova conexão
        conn = sqlite3.connect('database.db')
        # buscando um admin na tabela, que possua username e senha iguais aos que foram digitados pelo usuario
        logado = conn.execute("SELECT * FROM admin WHERE username=='%s' AND password=='%s'"%(uname, pwd))

        # verifica se a busca gerou algum resultado
        if logado.fetchone():
            # se gerou o login é feito
            message.set('Login efetuado com sucesso!!!')

        # caso contrário...
        else:
            # aviso ao usuario que tem parada errada
            message.set('Nome de usuario ou senha incorretos!!!')

def Loginform():
    # criando janela principal
    global janela_principal
    janela_principal = Tk()
    # mudando o título dajanela
    janela_principal.title("Login do Sistema")
    #alterando o tamanho da janela principal
    janela_principal.geometry('350x250')
    # alterando a cor da janela
    janela_principal['bg'] = '#1C2833'

    # criando variáveis globais
    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()

    # criando label título
    labelTitulo = Label(janela_principal, width=300, text='Formulário de login',
                        bg='#0E6655', fg='#fff', font=('Arial', '12', 'bold'))
    labelTitulo.pack()

    # criando label nomme usuário
    labelNome = Label(janela_principal, text='Nome de usuário', bg='#1C2833',
                      fg='#fff', font=('Arial', '12', 'bold'))
    labelNome.place(x=10, y=40)

    # criando caixa de texto onde será digitado o nome de usuário
    txtUsername = Entry(janela_principal, textvariable=username, bg='#1C2833',
                        fg='#fff', font=('Arial', '12', 'bold'))
    txtUsername.place(x=150, y=42)

    # criando label senha do usuário
    labelPassword = Label(janela_principal, text='Senha', bg='#1C2833',
                          fg='#fff', font=('Arial', '12', 'bold'))
    labelPassword.place(x=10, y=80)

    # criando caixa de texto onde será digitado o nome de usuário
    txtPassword = Entry(janela_principal, textvariable=password, bg='#1C2833',
                        fg='#fff', font=('Arial', '12', 'bold'), show='*')
    txtPassword.place(x=150, y=82)

    labelSaida = Label(janela_principal, text="", textvariable=message, bg='#1C2833',
                       fg='#fff', font=('Arial', '12', 'bold'))
    labelSaida.place(x=20, y=210)

    btnLogin = Button(janela_principal, text='Login', width=10, height=1, command=login,
                      bg='#0E5566', fg='white', font=('Arial', '12', 'bold'))
    btnLogin.place(x=125, y=170)
    janela_principal.mainloop()


Loginform()
