class Cafeteira:
    def __init__(self, iniVoltagem, initCapacidade):
        self.Voltagem = iniVoltagem  # atributo1
        self.Capacidade = initCapacidade  # atributi2

    def getVoltagem(self):
        return self.Voltagem

    def getCapacidade(self):
        return self.Capacidade

    def ligar(self):
        return True  # descrevo o que é feito ao ligar

    def desligar(self):
        return True  # descreve o que acontece ao desligar a cafeteira

p = Cafeteira(100, 1000)
q = Cafeteira(220, 1500)

print(q.getVoltagem())
print(p.getCapacidade())