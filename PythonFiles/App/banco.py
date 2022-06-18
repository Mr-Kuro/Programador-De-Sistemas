import sqlite3


class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        # conexao criaada
        self.createTable()
        # chamando o método

    def createTable(self):
        c = self.conexao.cursor()
        # cursor é para manipular o banco a a partir do python
        # c é a variavel de referência do bd
        # cursor é um método do sqlite3

        c.execute("""create table if not exists usuarios(
        idusuario integer primary key autoincrement, 
        nome text, 
        telefone text, 
        email text, 
        usuario text,
        senha text)""")
        # cria tabelas e colunas

        self.conexao.commit()
        # envia pro banco de dados
        c.close()

