class Tamagushi:
    def __init__(self, initNome, initIdade, initSaude, initSaciado):
        self.nome = initNome
        self.idade = initIdade
        self.saude = initSaude
        self.saciado = initSaciado

    def getNome(self):
        print(self.nome)
        return self.nome

    def getIdade(self):
        print(self.idade)
        return self.idade

    def getSaude(self):
        print(self.saude)
        return self.saude

    def getsaciado(self):
        print(self.saciado)
        return self.saciado

    def gethumor(self):
        print(self.saciado * self.saude)
        return self.saciado * self.saude

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def setSaude(self, valor):
        self.saude = valor

    def setsaciado(self, valor):
        self.saciado = valor

    def alimentar(self, valor):
        if 0 <= valor <= 100:
            if self.saciado == 100:
                print('Quantidade máxima de saciedade atingida')
            else:
                self.saude += self.saude * valor / 100
        else:
            print('Valor superior ou inferior ao limite de saciedade')

    def brincar(self, valor):
        if 0 <= valor <= 100:
            if self.saude == 100:
                print('Quantidade máxima de saúde atingida')
            else:
                self.saude += self.saude * valor / 100
        else:
            print('Valor superior ou inferior ao limite de saúde')

    def getAllAtributesTamagushi(self):
        print(f'Nome =>       {self.getNome()}\n'
              f'Idade=>       {self.getIdade()}\n'
              f'Saciedade =>  {self.getsaciado()}\n'
              f'Saúde =>      {self.getSaude()}\n'
              f'Humor =>      {self.gethumor()}')


# teste da classe
pou = Tamagushi('The Life Snake', 19, 60, 80)
pou.getNome()
pou.getIdade()
pou.getSaude()
pou.getsaciado()
pou.gethumor()

pou.setNome('Ricardão')
pou.setIdade(25)
pou.setsaciado(11)
pou.setSaude(2)

pou.getNome()
pou.getIdade()
pou.getSaude()
pou.getsaciado()
pou.gethumor()

pou.alimentar(20)
pou.getSaude()
pou.getAllAtributesTamagushi()
