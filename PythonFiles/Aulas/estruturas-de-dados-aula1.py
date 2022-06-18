# lista de números

#o 0 é a posição inicial
numeros = [1, 5, 8, 14, 22, 47, 56, 90, 99, 5, 7, 12, 5]

# numeros[0] = 5
# print(numeros)

# numeros.append(4) #adiciona um valor ao final da lista
# print(numeros)

# numeros.insert(0, 5) # o 0 é a posição, já o 5 é o valor que a posição vai assumir
# print(numeros)

# numero = [1, 2, 3, 2]
# numero.remove(1) # remove o primeiro número o numero dentro do parentese
# print(numero)

# apagado = numeros.pop(2) # o pop também retorna o número que apagou além de apagar
# print(apagado)

# numeros.clear() # clear remove todos os itens da lista
# print(numeros)

# indece = numeros.index(56, 5, 8) # procurar o índice do 56 do índice 5 até o índice 8
# print(indece)

# indice = numeros.count(5) #conta quantas vezes o elemento aparece na lista
# print(indice)

# numeros.sort() # ordena os elementos da lista em ordem crescente
# print(numeros) # para por em ordem decescente : numeros.sort(reverse=true)

# numeros.reverse()
# print(numeros)

# copia = numeros.copy() #copia a lista
# print(copia)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# # print(fruits.count('apple'))
# # print(fruits.count('tangerine'))
# # print(fruits.index('banana'))
# # print(fruits.index('banana', 4))
# print('')
# fruits.reverse()
# print(fruits)
# fruits.append('grape')
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.pop()
# print(fruits)
# # não se pode ordenar e nem  números comparar números com letras.

u = 1
i = numeros.index(u)
print(i)

print(fruits)
a = 'orange'
f = fruits.remove(a)
print(fruits)