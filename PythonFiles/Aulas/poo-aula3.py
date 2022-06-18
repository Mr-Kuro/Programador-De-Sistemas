class Retangulo:
    def __init__(self, initBase, initAltura):
        self.base = initBase
        self.altura = initAltura

        def getBase(self):
            return self.base

        def getAltura(self):
            return self.altura

        def detBase(self, baseNovo):
            self.base = baseNovo

        def setAltura(self, alturaNovo):
            self.altura = alturaNovo

        def calculaArea(self):
            return self.base * self.altura

        def calculaPerimetro(self):
            return 2 * self.base * self.altura


# teste da classe
print('Digite o valor da base')
base = float(input())
print('Digite o valor da altura')
altura = float(input())

terreno = Retangulo(base, altura)  # objeto terreno

print('A área do terreno é ', terreno.calculaArea())
print('O perímetro do terreno é ', terreno.calculaPerímetro())
