class Carro:
    def __init__(self, ):
        self.combustivel = 0
        self.consumo = 1

    def adicionarGasolina(self, combustivel):
        self.combustivel = combustivel

    def getCombustivel(self):
        print(self.combustivel)

    def andar(self, Km):
        andado = Km / self.consumo
        if andado < self.combustivel:
            self.adicionarGasolina(self.combustivel - andado)
        else:
            print('Tanque vazio!')


# Teste da Class Carro
fusca = Carro()
fusca.adicionarGasolina(20)
fusca.getCombustivel()
fusca.andar(10)
fusca.getCombustivel()

# resolução do professor

class Carro:

    def __init__(self, initConsumo):
        self.consumo = initConsumo
        self. qtdCombustivel =0

    def adicionarGasolina(self, quantidade):
        self.qtdCombustivel += quantidade

    def getGasolina(self):
        print(f'A quantidade de gasolina atual é: {self.qtdCombustivel}')
        return self.qtdCombustivel

    def andar(self, distancia):
        gasto = distancia / self.consumo
        if gasto <= self.qtdCombustivel:
            self.qtdCombustivel -= gasto
        else:
            print('Combustivel insuficiente para percurso')


# teste da classe

meuFusca = Carro(15)
# 15 Km com 1 litro

meuFusca.adicionarGasolina(20)
# abastece com 20 litros de combustível

meuFusca.andar(100)
# anda 100 Km

meuFusca.getCombustivel()