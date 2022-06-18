# python -m pip install pyinstaller
# pip installer pyinstaller
# pyinstaller --onefile --windowed --noconsole App.py

import sqlite3 as sql

class TransectionObject():
    database = "clientes.db"
    conn = None  # conexão
    cur = None  # para mexer no banco
    connected = False

    # método para criar conexão com o banco
    def connect(self):
        TransectionObject.conn = sql.connect(TransectionObject.database)
        TransectionObject.cur = TransectionObject.conn.cursor()
        TransectionObject.connected = True

    # método para fechar conexão com o banco
    def disconnect(self):
        TransectionObject.conn.close()
        TransectionObject.connected = False

    # metodo executa comando no banco de dados recebe 3 comandos
    # self
    # sql = comando que vai ser executado
    # parme = vetor com os parametros do comando
    def execute(self, sql, parms = None):
        # verificando se a conexão  está ativa
        if TransectionObject.connected:
            # verificando se não há parametros
            if parms == None:
                TransectionObject.cur.execute(sql)
            else:
                TransectionObject.cur.execute(sql, parms)
                return True
        else:
            return False

    # método que recupera os valores recebidos de um comando
    def fechall(self):
        return TransectionObject.cur.fetchall()

    # método que realixa o commit das operações realizadas
    def persist(self):
        # verificando se conexão está ativa
        if TransectionObject.connected:
            TransectionObject.conn.commit()
            return True
        else:
            return False

# função para iniciar banco de dados
def initDB():
    # criando objeto para usar os métodos criados acima
    trans = TransectionObject()
    # conectando ao banco de dados
    trans.connect()
    # executando comando de criar tabela
    trans.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    # fechar conexão
    trans.disconnect()

initDB()

def view():
    # criando objeto para usar os métodos criados acima
    trans = TransectionObject()
    # conectando ao banco
    trans.connect()
    # executando o comando de selecionar todos os clientes
    trans.execute("SELECT * FROM clientes")
    # Recuperando os valores
    rows = trans.fechall()
    # fechar conexão
    trans.disconnect()
    # Retornando os valores
    return rows

def insert(nome, sobrenome, email, cpf):
    # criando objeto para usar os métodos criados acima
    trans = TransectionObject()
    # conectando ao banco
    trans.connect()
    # executar comando de inserir clientes
    trans.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
    # persistir inserção na tabela
    trans.persist()
    # fechar conexão
    trans.disconnect()

def search(nome='', sobrenome="", email="", cpf=""):
    # criando objeto para usar os métodos criados acima
    trans = TransectionObject()
    # conectando ao banco
    trans.connect()
    # executar comando de buscar um cliente na tabela
    trans.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome =? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
    # Recuperando os valores
    rows = trans.fechall()
    # fechar conexão
    trans.disconnect()
    # Retornando os valores
    return rows

def update(id, nome, sobrenome, email, cpf):
    # criando objeto para usar os métodos criados acima
    trans = TransectionObject()
    # conectando ao banco
    trans.connect()
    # executando xomando de atualizar um cliente na tabela
    trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
    # persistir a alteração na tabela
    trans.persist()
    # fechar conexão
    trans.disconnect()

def delete(id):
    # criando objeto para usar os métodos criados acima
    trans = TransectionObject()
    # conectando ao banco
    trans.connect()
    # executando comando de apagar um cliente na tabela
    trans.execute("DELETE FROM clientes WHERE id=?", (id, ))  # a vírgula é proposital para dizer ao python que é apenas um parametro pois o parms é uma lista
    # persistir as alterações
    trans.persist()
    # fechar conexão
    trans.disconnect()
