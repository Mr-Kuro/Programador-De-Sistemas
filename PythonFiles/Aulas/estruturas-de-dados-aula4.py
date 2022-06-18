# PILHA
# append - adiciona no final
# pop - adiciona no final

stack = [3, 4, 5,]

stack.append(6)
stack.append(7)

print(stack)

removido = stack.pop()
print(removido)
print(stack)

removido = stack.pop()
print(removido)
print(stack)

removido = stack.pop()
print(removido)
print(stack)

print('')
print('')

# FILA = QUEUE
# enqueue = enfileira
# dequeue = desenfileira
# append - insere no final
# pop(0) remove no início
# se alguém tem prioridade: insert(0, 0) - elemento, posição

# para deixar mais rápido: deque
# from collections import deque
from collections import deque
# declarando:
qu = deque(['Eric', 'Jhon', 'michael'])

# inserindo:
qu.append('Terry')
qu.append('Graham')

# removendo:
qu.popleft()
qu.pop()

# resultado:
print(qu)

print('')
print('')

# Tupla
# os dados não podem ser alterados
# numeros = (1, 2, 3)
# got = ('Game of Thrones', 2011, 2019, 9.4)
#  index, count, copy
# tupla[-1] mostra o último elemento da lista
# tupla[:3] a tupla irá mostrar de 0  à 3
# tupla[-4:]
empresas = ['Google', 'Facebook', 'Amazon']
empresas[1] = 'samsung'  # não funfa pois a tupla é imutável

# CONJUNTOS
# não pode conter elementos duplicados
# x = set() conjunto se, elementos
# x = {1, 2, 3}  conjunto com elementos

# lista = [1, 3, 5, 7, 3, 9]
# x = set()
# for i in lista:
#     if i not in x:
#         x.add(i)
#     else:
#         print('Elemento repetido:', i)
# print(x)

# numeros = {1, 2, 3, 4}
#
# numeros.update([3, 4, 5, 6])  # adiciona vários elementos ao set
# print(numeros)
# numeros.discard(2)
# print(numeros)

a = set('abracadabra')
b = set('alakazam')
print(a)
print(b)
# print(a - b)  # contido em a diferente de b
# print(a | b)  # a unido a b
# print(a & b)  # intercessão - elementos que estão nos conjutos
print(a ^ b)  # diferença simétrica