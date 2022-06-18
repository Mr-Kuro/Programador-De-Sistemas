#QUANTIDADE DE NÚMEROS E LETRAS DO INPUT
print('')
print('digite o que desejar, ó caro usuário:')

recapcha = 0
lista = 0
digit = 0
alpha = 0
special = 0

lista = input()

for recapcha in lista:
    if recapcha.isdigit():
        digit += 1
    elif recapcha.isalpha():
        alpha += 1
    else:
        special += 1

print(f'Quantiidade de letras: {alpha}')
print(f'Quantidade de números: {digit}')
print(f'Quantidade de símbolos: {special}')
