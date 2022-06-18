import random

class ContaInvestimento:
    def __init__(self, initNumeroConta, initInvestidor):
        self.conta = initNumeroConta
        self.nome = initInvestidor
        self.saldo = 0.0
        self.taxaJuros = 00

    def deposito(self, novosaldo):
        self.saldo += novosaldo

    def saque(self, novosaldo):
        self.saldo -= novosaldo

    def getSaldoo(self):
        print(self.saldo)
        return self.saldo

    def getNomee(self):
        print(self.nome)
        return self.nome

    def getConta(self):
        print(self.conta)
        return self.conta


    def correrJuros(self):
        self.saldo += self.saldo * self.taxaJuros / 100

    def setSaldo(self, valor):
        self.saldo = valor

    def setJuros(self, juros):
        self.taxaJuros = juros


# teste da class
ricardo = ContaInvestimento(random.randint(100000, 999999), 'Ricardo Molusketi')
ricardo.setSaldo(1000)
ricardo.getNomee()
ricardo.getConta()
ricardo.getSaldoo()
ricardo.setJuros(10)

ricardo.correrJuros()
ricardo.getSaldoo()
ricardo.correrJuros()
ricardo.getSaldoo()
ricardo.correrJuros()
ricardo.getSaldoo()
ricardo.correrJuros()
ricardo.getSaldoo()
ricardo.correrJuros()
ricardo.getSaldoo()


# resolução do professor

class ContaInvestimento:
    def __init__(self, initNumero, initConta, initTaxaJuros):
        self.conta = initNumero
        self.nome = initConta
        self.saldo = 0.0
        self. taxaJuros = initTaxaJuros

    def alterarNome(self, nomeCorrentista):
        self.nome = nomeCorrentista

    def depositar(self, valor):
        self.saldo = valor

    def sacar(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100))


# teste da classe
conta = ContaInvestimento(64729, 'Ícaro', 1)
conta.depositar(1000)
print(f'\n{conta.nome}\n{conta.conta}\n{conta.saldo}')
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)