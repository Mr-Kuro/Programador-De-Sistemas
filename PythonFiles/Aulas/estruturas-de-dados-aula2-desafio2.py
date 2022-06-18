# aqui pegamos os elementos de duas listas e criamos uma lista intercalada

frutas = []
carnes = []
lista3 = []

print('informe os valores da primeira lista')
for i in range(0, 5):
    frutas.append(input())

print('informe os valores da segunda lista')
for i in range(0,5):
    carnes.append(input())

for i in range(0,5):
    lista3.append(frutas[i])
    lista3.append(carnes[i])
print(lista3)

# print('')
# print('Crie as alista.')
#
# lista_par = []
# lista_impar = []
# lista_resultante = []
#
# for i in range(1, 6):
#     print(f'Lista de números pares. índece {i}')
#     lista_par.append(int(input()))
#
# for i in lista_par:
#     if i % 2 != 0:
#         print(f'A lista {lista_par} não contem apenas números pares')
#
# print('Agora os números ímpares')
#
# for i in range(1, 6):
#     print(f'Lista de números impares. índece {i}')
#     lista_impar.append(int(input()))
# for i in lista_par:
#     if i % 2 == 0:
#         print(f'A lista {lista_impar} não contem apenas números ímpares')
#
# a = 0
# b = 0
#
# for a in lista_par and b in lista_impar:
#     lista_resultante.append(a)
#         lista_resultante.append(b)

# print('')
# print(lista_resultante)