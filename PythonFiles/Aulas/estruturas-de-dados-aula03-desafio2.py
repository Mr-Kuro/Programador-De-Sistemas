import random

# # importando bibliotecas
# numeros = []
#
# for i in range(0, 10):
#     ram = random.randint(1,6)
#     numeros.append(ram)
#
# print(numeros)
#
# for i in range(1, 11):
#     print(f' {i} -- {numeros.count(i)}')

import random

dado = [0]*6
numeros = []

for i in range(0, 10):
    numero = random.randint(0,5)
    numeros.append(numero + 1)
    dado[numero] +=1


print(numeros)

for i in range (0,6):
    print('%d - %d' % (i + 1, dado[i]))
