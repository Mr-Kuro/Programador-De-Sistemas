# python -m pip install pyinstaller
# pip installer pyinstaller
# pyinstaller --onefile --windowed --noconsole App.py

# CROD -> criar, ler, alterar, deletar <-

import sqlite3

class Database:
    def __init__(self, db):
        # criando a conexão com o banco
        self.con = sqlite3.connect(db)
        # criando o cursor para as operações com o banco
        self.cur = self.con.cursor()
        # comando para criar a tabela de funcionarios
        sql = """CREATE TABLE IF NOT EXISTS funcionarios(
        id INTEGER PRIMARY KEY, 
        nome TEXT,
        idade INTEGER,
        data TEXT,
        email TEXT,
        genero TEXT,
        telefone TEXT,
        endereco TEXT)"""
        # executando o comando acima
        self.cur.execute(sql)
        # persistindo o que foi feito
        self.con.commit()

    # método de inserir novco funcionário
    def insert(self, nome, idade, data, email, genero, telefone, endereco):
        # executando o comando ede inserir o comando de inserir novo funcionário na tabela de funcionario de banco de dados
        self.cur.execute("INSERT INTO funcionarios VALUES(NULL, ?, ? , ?, ?, ?, ?, ?)",
                         (nome, idade, data, email, genero, telefone, endereco))
        # persistindo o usuario que foi inserindo
        self.con.commit()

    # método para recuperar todos os funcionarios dados do banco
    def fetch(self):
        # executando o comando de recuperar todos os funcionarios
        self.cur.execute("SELECT * FROM funcionarios")
        # recupera os funcionarios e dalva na lista
        rows = self.cur.fetchall()
        return rows

    # método que deleta um registro no banco de dados
    def remove(self, id):
        # executando o comando de deletar um fuincionario
        self.cur.execute("DELETE FROM funcionarios WHERE id=?", (id, ))
        # persistindo o usuario que foi deletado
        self.con.commit()

    # método que atualiza um registro no banco de dados
    def update(self, idu, nome, idade, data, email, genero, telefone, endereco):
        # executando o comando de atualizar um funcionário do banco de dados
        self.cur.execute("UPDATE funcionarios SET nome=?, idade=?, data=?, email=?, genero=?, telefone=?, endereco=? WHERE id=?",
                         (nome, idade, data, email, genero, telefone, endereco, idu))
        # persistindo a alteração no usuario
        self.con.commit()
        