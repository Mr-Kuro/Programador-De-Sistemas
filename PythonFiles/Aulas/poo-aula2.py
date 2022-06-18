# um programa que vende café, ele recebe cupons e ele sempre vai tenta o maior café que seu cupom pode pagar

pequeno = 2
medio = 5
grande = 6

print('De quanto é seu cupom?')
cupom = input()

#  verifica se o cupom é válido
if cupom.isdigit():
    cupom = int(cupom)
else:
    print('Insira um cupom válido')
    exit()

# faz a venda e dá o troco
if cupom >= grande:
    print('Você pode pagar pelo café grande')
    if cupom == grande:
        print('Compra concluida')
    else:
        print('Seu troco é', cupom - grande)
elif cupom == medio:
    print('Você pode pagar pelo café médio.')
    print('Compra concluída!')
elif cupom >= pequeno:
    print('Você pode pagar pelo café pequeno')
    if cupom == pequeno:
        print('Compra concluída')
    else:
        print('Seu troco é', cupom - pequeno)
exit()


# poo:
class Cafe:
    # Construtor
    def __init__(self, initTamanho, initPreco):
        self.tamanho = initTamanho
        self.preco = initPreco

        # Checa se o cupom é válido
        def ChecaCupom(self, cupom):
            if cupom.isdigit():
                cupom = int(cupom)
                return cupom
            else:
                print('Insira um cupom válido')
                exit()

        # calcula o troco
        def darTroco(self, cupom):
            troco = cupom - self.preco
            return troco

        #  faz a venda
        def vender(self, cupom):
            cupom = self.ChecaCupom(cupom)
            if cupom >= self.preco:
                print('Você pode pagar pelo café', self.tamanho)
                if cupom == self.preco:
                    print('Compra concluida!')
                    cupom = 0
                else:
                    cupom = self.darTroco(cupom)
                    print('Seu troco é ', cupom)
                print('Obrigado pela preferência')