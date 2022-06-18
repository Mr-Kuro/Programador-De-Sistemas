# PAR OU ÍMPAR?
print('')
print('PAR OU ÍMPAR?')
print('Digite os numeros')

# num = 0
# contador = 9
#
# impar = 0
# par = 0
# # for i in range(contador):
# #     num = float(input())
# #     num = num % 2
# #     if num != 0: # o == serve para comparar dois números
# #         par += 1
# #     else:
# #         impar += 1
# # print(f'{impar} números são ímpares e {par} são pares.')

contadorpar = 0
contadorimpar = 0
numeros = (1, 2, 14, 4, 5, 6, 7, 8, 10)
for x in numeros:
#repete os números da lista numeros
    if (x % 2) == 0:
        contadorpar += 1
    else:
        contadorimpar += 1
print(f'A quantidade de números pares é {contadorpar}')
print(f'A quantidade de números ímpares é {contadorimpar}')
