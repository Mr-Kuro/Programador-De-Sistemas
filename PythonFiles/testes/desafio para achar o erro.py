# programa do fernando
class Carro:

    def __init__(self, initkml):
        self.kml = initkml
        self.combustivel = 0

    def getAndar(self, distancia):
        gasto = (distancia / self.kml)
        if (gasto <= self.combustivel):
            print("O combustivel gasto foi", gasto)
            self.combustivel -= gasto
        else:
            print("Combustivel insuficiente")

    def setAbastecer(self, combustivel):
        self.combustivel += combustivel

    def getCombustivel(self):
        print(self.combustivel)


carro1 = Carro(13)
carro2 = Carro(15)
carro1.getCombustivel()
carro1.setAbastecer(100)
carro1.getCombustivel()
carro1.getAndar(400)
carro1.getCombustivel()
print('')
carro2.setAbastecer(100)
carro2.getAndar(800)
carro2.getCombustivel()
