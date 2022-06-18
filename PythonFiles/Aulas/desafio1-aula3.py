# CAUCULAR A SOMA E A MÉDIA
print('')
print('Digite os números. Digite 0 para sair')

contador = 0
soma = 0
media = 0
num = 1

while num != 0:
   num = int(input())
   soma = soma + num
   contador += 1 # contador = contador + 1

print(f'A soma é: {soma}')
media = soma / (contador - 1)
print(f'A média é {media}')
