class Pessoa:
    # define os valores iniciais de classe (método construtor)
    def __init__(self, initNome, initIdade, initPeso, initAltura):
        self.nome = initNome
        self.idade = initIdade
        self.peso = initPeso
        self.altura = initAltura

    # métodos
    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer()

    def engordar(self, engordar):
        self.peso += engordar

    def emagrecer(self, emagrecer):
        self.peso -= emagrecer

    def crescer(self,):
        self.altura += 0.05

pessoa1 = Pessoa('Reinan Sales Portela', 19, 57, 1.79)

print(f'Deseja envelhecer {pessoa1.nome} em 1 ano?')
condicao = input()
if condicao.lower() == 's' or condicao.lower() == 'sim':
    pessoa1.envelhecer()
print(f'Quantos Kg deseja atribuir para engordar {pessoa1.nome}?')
engordar = float(input())
pessoa1.engordar(engordar)
print(f'Quantos Kg deseja diminuir para emagrecer {pessoa1.nome}?')
emagrecer = float(input())
pessoa1.emagrecer(emagrecer)
print(f'Deseja atribuir 0.5 a altura de {pessoa1.nome}?')
condicao = input()
if condicao.lower() == 'sim' or condicao.lower() == 's':
    pessoa1.crescer()
print(f'{pessoa1.nome}\n{pessoa1.idade}\n{pessoa1.peso}\n{pessoa1.altura:.2f}')
