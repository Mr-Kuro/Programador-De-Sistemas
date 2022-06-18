from banco import Banco


class Usuarios:

    def __init__(self):
        self.info = {}
        self.idusuario = 0
        self.nome = ''
        self.telefone = ''
        self.email = ''
        self.usuario = ''
        self.senha = ''

    def insertUser(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios(nome, telefone, email, usuario, senha) values('"
                      + self.nome + "', '"
                      + self.telefone + "', '"
                      + self.email + "', '"
                      + self.usuario + "', '"
                      + self.senha + "')")
            banco.conexao.commit()
            c.close()
            return 'Usuário cadastrado com sucesso'

        except:
            return 'Ocorreu um erro na incerção do usuário'

    def updateUser(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()
            c.execute("update usuarios set nome = '" +
                      self.nome + "', telefone = '" +
                      self.telefone + "', email = '" +
                      self.email + "', usuario = '" +
                      self.usuario + "', senha = '" +
                      self.senha + "' where idusuario = " + self.idusuario + "")
            banco.conexao.commit()
            c.close()
            return 'Usuário atualizado com sucesso!'

        except:
            return 'Ocorreu um erro na alteração do usuário'

    def deleteUser(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()
            c.execute("delete from usuarios where idusuario =" + self.idusuario + "")
            banco.conexao.commit()
            c.close()
            return 'Usuario deletado com sucesso!'

        except:
            return 'Ocorreu um erro na exclussão do usuário'

    def selectUser(self, usuarioId):
        banco = Banco()

        try:
            c = banco.conexao.cursor()
            c.execute("select * from usuarios where idusuario =" + usuarioId + "")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()
            return 'Busca feita com sucesso!'

        except:
            return 'Ocorreu um erro na busca do usuário'
