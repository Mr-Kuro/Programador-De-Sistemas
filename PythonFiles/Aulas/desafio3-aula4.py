#FIBONACCI DOS NÚMEROS
print('')
print('Para  calcular o fibonacci,  digite um número.')

a = 0
b = 1
c = 0
contador = 0

num = int(input())

while contador < num:
    c = a + b
    a = b
    b = c
#aqui é onde a mágica acontece, meu caro!
    contador +=1
print(a)


