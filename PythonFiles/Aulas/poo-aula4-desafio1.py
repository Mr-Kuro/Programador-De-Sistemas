class Funcinario:
    def __init__(self):
        self.nome = 'Guest'
        self.salario = 0

    def setNome(self, nome):
        self.nome = nome

    def setSalario(self, salario):
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentaSalario(self, aumento):
        self.salario += self.salario * aumento / 100

funcionario1 = Funcinario()
print(funcionario1.getNome())
print('R$',funcionario1.getSalario())

print('\nQual o nome do funcionario?')
nome = input()
funcionario1.setNome(nome)
print(f'Qual o salário de {funcionario1.getNome()}?')
salario = int(input())
funcionario1.setSalario(salario)

print(f'Deseja dar um aumento para {funcionario1.getNome()}?')
condicao = input()
if condicao.lower() == 'sim':
    print('Quantos % de aumento?')
    aumento = int(input())
    funcionario1.aumentaSalario(aumento)

print(f"Nome: {funcionario1.nome}\n"
      f"salário: R${funcionario1.salario:.2f}")
