class Macaco:
    def __init__(self, initNome):
        self.nome = initNome
        self.estomago = []

    def comer(self, comeu):
        self.estomago.append(comeu)

    def digerir(self):
        if len(self.estomago) > 0:
            self.estomago.pop(0)

    def verEstomago(self):
        print(self.estomago)


macaco = Macaco('Macaco')
print(macaco.verEstomago())
macaco.comer('laranja')
macaco.comer('tangerina')
macaco.comer('amendoim')
macaco.verEstomago()
print('')

macacoCanibal = Macaco('Macaco Canibal')
print(macacoCanibal.verEstomago())
macacoCanibal.comer('laranja')
macacoCanibal.comer('tangerina')
macacoCanibal.comer(macaco)
macacoCanibal.digerir()
macacoCanibal.verEstomago()
