class BombaCombustível:
    def __init__(self, initTipoCombustivel, initValorLitro, initQuantidadeCombustivel):
        self.tipoCombustível = initTipoCombustivel
        self.valorLitro = initValorLitro
        self.quantidadeCombustivel = initQuantidadeCombustivel

    def abastecerPorValor(self, valor):
        if self.quantidadeCombustivel > valor > 0:
            self.quantidadeCombustivel -= 0.1 * valor
            print(f'Por R${valor:.2f} foram acrescentados {self.valorLitro * 0.01 * valor:.2f} litros de {self.tipoCombustível} no veículo.')
            print(f'Restam {self.quantidadeCombustivel:.2f} litros de {self.tipoCombustível} na bomba de {self.tipoCombustível}.')

    def abastecerPorLitro(self, valor):
        if self.quantidadeCombustivel >= valor > 0:
            self.quantidadeCombustivel -= valor
            print(f'Você deve pagar R${valor * self.valorLitro:.2f} pelos {valor:.2f} litros de gasolina depositados no veículo.')
            print(f'Restam {self.quantidadeCombustivel:.2f} litros de {self.tipoCombustível} na bomba de {self.tipoCombustível}.')

    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, valor):
        self.tipoCombustível = valor

    def alterarQantidadeCombustivel(self, valor):
        self.quantidadeCombustivel = valor


print('')

bomba1 = BombaCombustível('Gasolina', 10.00, 100)
bomba1.abastecerPorValor(15)
print(bomba1.quantidadeCombustivel)  # testar se a quantidade de combustivel foi alterada

print('')
bomba1.abastecerPorLitro(1.5)
print(bomba1.quantidadeCombustivel)  # testar se a quantidade de combustivel foi alterada


print('')
bomba1.alterarValor(20)
print(bomba1.valorLitro)  #testar se o valor do combustivel foi alterado

bomba1.alterarCombustivel('Etanol')
print(bomba1.tipoCombustível)  #testar se o tipo de combustivel foi alterado

bomba1.alterarQantidadeCombustivel(100)
print(bomba1.quantidadeCombustivel)   #testar se a quantidade de combustivel foi alterada

print('')

# Resolução do professor

class BombaCombustivel:
    def __init__(self, initTipoCombustivel, initValorLitro, initQuantidadeCombustivel):
        self.tipoCombustivel = initTipoCombustivel
        self.valorLitro = initValorLitro
        self.quantidadeCombustivel = initQuantidadeCombustivel

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = valorLitro

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        if totalLitros <= self.quantidadeCombustivel:
            self.setQuantidadeCombustivel(self.quantidadeCombustivel - totalLitros)
            print(f' {totalLitros} litros')

    def abastecerPorLitro(self, qtdLitro):
        valor = qtdLitro * self.valorLitro
        if qtdLitro <= self.quantidadeCombustivel:
            self.setQuantidadeCombustivel(self.quantidadeCombustivel - qtdLitro)
            print(f'Custou R${valor:.2f}')


# teste
bomba1 = BombaCombustivel('Gasolina Aditivada', 6.99, 100)
bomba1.abastecerPorValor(100)
bomba1.abastecerPorLitro(20)
bomba1.setValorLitro(6.59)
bomba1.abastecerPorValor(100)
bomba1.abastecerPorLitro(20)
print(bomba1.quantidadeCombustivel)
bomba1.setQuantidadeCombustivel(100)
print(bomba1.quantidadeCombustivel)
bomba1.setTipoCombustivel('Alcool')
print(bomba1.tipoCombustivel)