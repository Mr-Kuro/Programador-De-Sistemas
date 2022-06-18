# FUNÇÕES
# def NOME( PARAMETROS):

#     COMANDOS
# def hello(meu_nome):
#     print(f'Olá, {meu_nome}')
#
# hello('ícaro')

# def minha_funcao():
#     frase = 'Olá, mundo'
#     return frase
#
# print(minha_funcao())

# def hello(nome, idade):
#     print(f'Olá, {nome}\nSua idade é {idade}')
# hello('je', 15)



def calculaPagamento(qtdHoras, valor_hora):
    horas = float(qtdHoras)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas*taxa
    else:
        extra = horas - 40
        salario = 40*taxa+(extra*(1.5*taxa))
    return salario

print('')
print('Digite as horas trabalhadas')
strHoras = input()
print('Digite o valor da hora trabalhada')
strValor = input()

totalSalario = calculaPagamento(strHoras, strValor)
print(f'O valor dos seus rendimentos é de R${totalSalario}')


# def cauculoIMC(peso, altura):
#     print(peso/ altura **2)
#
# # calculoIMC(85, 1.90)
# # cauculoIMC(peso = 85, altura = 1.90)
# cauculoIMC(altura = 1.90, peso = 85)
