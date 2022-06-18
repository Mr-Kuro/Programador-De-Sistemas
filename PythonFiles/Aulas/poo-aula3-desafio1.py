import random

class ContaCorrente:
    def __init__(self, initNumeroConta, initNomeCorrentista):
        self.Conta = initNumeroConta
        self.nome = initNomeCorrentista
        self.saldo = 0.0

    def deposito(self, novosaldo):
        self.saldo += novosaldo

    def saque(self, novosaldo):
        self.saldo -= novosaldo

    def getSaldoo(self):
        return self.saldo

    def getNomee(self):
        return self.nome

    def getConta(self):
        return self.saldo

print('Digite o nome completo do cliente')
nome = input()
conta = random.randint(100000, 999999)

cliente1 = ContaCorrente(conta, nome)

condicao = 'sim'
while condicao.lower() == 'sim':
    print('Deseja fazer um deposito??')
    rdeposito = input()

    if rdeposito.lower() == 'sim':
        print('Quanto deseja depositar?')
        deposito = input()
        novoS = cliente1.deposito

    print('Deseja fazer um saque??')
    rsaque = input()
    if rsaque.lower() == 'sim':
        print('Quanto deseja sacar?')
        saque = input()
        if saque > cliente1.saldo:
            novoS = cliente1.saque

    print('deseja alterar mais algo?')
    condicao = input()


print('Operação concluida')


# resploção do professor:



class Conta():
    def __init__(self, initNome, initNumero):
        self.nome = initNome
        self.numero = initNumero
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print('Saldo insuficiente')
            exit()
            return False

    def getSaldo(self):
        return self.saldo

    def getNome(self):
        return self.nome

    def getSaldo(self):
        return self.saldo

# teste da classe
print('Digite o nome')
usuario = input()
numeroConta = random.randint(100000, 999999)

conta1 = Conta(usuario, numeroConta)
print(f'Conta de {conta1.getNome()} foi Criada com sucesso\n')

r1 = ''
r2 = ''

while True:
    print('Deseja fazer um deposito?')
    r1 = input()
    if r1.lower() == 'sim':
        print('Qual o valor do depósito?')
        valor = float(input())
        conta1.depositar(valor)
        print(f'Saque realizado. O saldo disponível é de: {conta1.getSaldo()}')

    print('Deseja fazer um saque?')
    r2 = input()
    if r2 .lower() == 'sim':
        print('Qual o valor do saque?')
        valor = float(input())
        conta1.sacar(valor)
        sucesso = conta1.sacar(valor)
        if sucesso == True:
            print(f'Saque realizadoSaldo disponível é de: {conta1.getSaldo()}')
    else:
        break

