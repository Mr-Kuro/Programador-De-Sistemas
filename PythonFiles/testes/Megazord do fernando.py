# Funcionamento Padrão
class BombaCombustivel:

    def __init__(self, initTipo, initQuantidade, initValor):
        self.tipo = initTipo
        self.quantidade = initQuantidade
        self.valor = initValor

    def abastecerPorValor(self, dinheiro):
        pedido = (dinheiro / self.valor)
        if (self.quantidade >= pedido):
            self.setAlterarQuantidade(self.quantidade - pedido)
            print("Veiculo abastecido com:", self.tipo)
            print("Valor unitario:", self.valor)
            print("Quantidade de combustivel vendida:", pedido)
            print("Restante na bomba:", self.quantidade)
        else:
            print("Quantidade insuficiente na bomba.")

    def abastecerPorUnidade(self, unidade):
        pedido = (self.valor * unidade)
        if (self.quantidade >= unidade):
            self.setAlterarQuantidade(self.quantidade - unidade)
            print("Veiculo abastecido com:", self.tipo)
            print("Valor unitario:", self.valor)
            print("Quantidade vendida em R$:", pedido)
            print("Restante na bomba:", self.quantidade)
        else:
            print("Quantidade insuficiente na bomba.")

    def setAlterarValor(self, valor):
        self.valor = valor

    def setAlterarCombustivel(self, tipo):
        self.tipo = tipo

    def setAlterarQuantidade(self, quantidade):
        self.quantidade += quantidade


bomba1 = BombaCombustivel("Alcool", 100.0, 5.5)
bomba2 = BombaCombustivel("Diesel", 100.0, 3)
bomba3 = BombaCombustivel("gasolina", 100.0, 7)
bomba4 = BombaCombustivel("GNV", 100.0, 4.2)

conteudoBomba1 = "Alcool"
conteudoBomba2 = "Diesel"
conteudoBomba3 = "Gasolina"
conteudoBomba4 = "GNV"

# Area do cliente.
print("Escolha um combustivel.")
print("[1] => ", conteudoBomba1)
print("[2] => ", conteudoBomba2)
print("[3] => ", conteudoBomba3)
print("[4] => ", conteudoBomba4)
print("[0] => Area do funcionario")
resposta = float(input())
if (resposta == 1):
    print("Como prefere comprar?")
    print("[1]unidades ou [2]valores")
    compra = float(input())
    if (compra == 1):
        print("Digite o valor")
        unidade = float(input())
        bomba1.abastecerPorUnidade(unidade)

    elif (compra == 2):
        print("Digite o valor")
        dinheiro = float(input())
        bomba1.abastecerPorValor(dinheiro)

elif (resposta == 2):
    print("Como prefere comprar?")
    print("[1]unidades ou [2]valores")
    compra = float(input())

    if (compra == 1):
        print("Digite o valor")
        unidade = float(input())
        bomba2.abastecerPorUnidade(unidade)

    elif (compra == 2):
        print("Digite o valor")
        dinheiro = float(input())
        bomba2.abastecerPorValor(dinheiro)

elif (resposta == 3):
    print("Como prefere comprar?")
    print("[1]unidades ou [2]valores")
    compra = float(input())

    if (compra == 1):
        print("Digite o valor")
        unidade = float(input())
        bomba3.abastecerPorUnidade(unidade)

    elif (compra == 2):
        print("Digite o valor")
        dinheiro = float(input())
        bomba3.abastecerPorValor(dinheiro)

elif (resposta == 4):
    print("Como prefere comprar?")
    print("[1]unidades ou [2]valores")
    compra = float(input())

    if (compra == 1):
        print("Digite o valor")
        unidade = float(input())
        bomba4.abastecerPorUnidade(unidade)

    elif (compra == 2):
        print("Digite o valor")
        dinheiro = float(input())
        bomba4.abastecerPorValor(dinheiro)

# Area do funcionario.

elif (resposta == 0):
    print("Informe a senha de acesso:")
    senha = float(input())
    if (senha == 6842):
        print("Lista de Alterações")
        print("[1] => Alteração de tipo de combustivel.")
        print("[2] => Incluir reabastecimento de bomba.")
        print("[3] => Alterar preço do combustivel.")
        altc = float(input())
        if (altc == 1):
            print("Informe a bomba [1 a 4]")
            bomba = float(input())
            if (bomba != 1) and (bomba != 2) and (bomba != 3) and (bomba != 4):
                print("Comando invalido.")
            else:
                print("informe o novo combustivel.")
                novovalor = str(input())
                if (bomba == 1):
                    bomba1.setAlterarCombustivel(novovalor)
                    conteudoBomba1 = novovalor
                    print("Novo combustivel da Bomba 1:", bomba1.tipo)

                elif (bomba == 2):
                    bomba2.setAlterarCombustivel(novovalor)
                    conteudoBomba2 = novovalor
                    print("Novo combustivel da Bomba 2:", bomba2.tipo)

                elif (bomba == 3):
                    bomba3.setAlterarCombustivel(novovalor)
                    conteudoBomba3 = novovalor
                    print("Novo combustivel da Bomba 3:", bomba3.tipo)

                elif (bomba == 4):
                    bomba4.setAlterarCombustivel(novovalor)
                    conteudoBomba4 = novovalor
                    print("Novo combustivel da Bomba 4:", bomba4.tipo)

        elif (altc == 2):
            print("Informe a bomba [1 a 4]")
            bomba = float(input())
            if (bomba != 1) and (bomba != 2) and (bomba != 3) and (bomba != 4):
                print("Comando invalido.")
            else:
                print("informe o valor reabastecino na bomba.")
                novovalor = float(input())
                if (bomba == 1):
                    if ((bomba1.quantidade + novovalor) <= 500):
                        bomba1.setAlterarQuantidade(novovalor)
                        print("Novo quantitativo", bomba1.quantidade)
                    else:
                        print("Volume não suportado")

                elif (bomba == 2):
                    if ((bomba2.quantidade + novovalor) <= 500):
                        bomba2.setAlterarQuantidade(novovalor)
                        print("Novo quantitativo", bomba2.quantidade)
                    else:
                        print("Volume não suportado")

                elif (bomba == 3):
                    if ((bomba3.quantidade + novovalor) <= 500):
                        bomba3.setAlterarQuantidade(novovalor)
                        print("Novo quantitativo", bomba3.quantidade)
                    else:
                        print("Volume não suportado")

                elif (bomba == 4):
                    if ((bomba4.quantidade + novovalor) <= 500):
                        bomba4.setAlterarQuantidade(novovalor)
                        print("Novo quantitativo", bomba4.quantidade)
                    else:
                        print("Volume não suportado")

        elif (altc == 3):
            print("Informe a bomba [1 a 4]")
            bomba = float(input())
            if (bomba != 1) and (bomba != 2) and (bomba != 3) and (bomba != 4):
                print("Comando invalido.")
            else:
                print("informe o novo preço do combustivel")
                novovalor = str(input())
                if (bomba == 1):
                    bomba1.setAlterarValor(novovalor)
                    print("Novo preço do combustivel na Bomba 1:", bomba1.valor)

                elif (bomba == 2):
                    bomba2.setAlterarValor(novovalor)
                    print("Novo preço do combustivel na Bomba 2:", bomba2.valor)

                elif (bomba == 3):
                    bomba3.setAlterarValor(novovalor)
                    print("Novo preço do combustivel na Bomba 3:", bomba3.valor)

                elif (bomba == 4):
                    bomba4.setAlterarCombustivel(novovalor)
                    print("Novo preço do combustivel na Bomba 4:", bomba4.valor)

        else:
            print("Comando invalido.")
    else:
        print("Acesso Negado.")
else:
    print("Comando invalido.")