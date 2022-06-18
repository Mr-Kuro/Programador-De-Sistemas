# a função irá averiguar se o número digitado está na lista

def iflista(lista, numero):
    numero = float(numero)
    for i in lista:
        if numero == i:
            return True
        else:
            return False


print('Digite o número que deseja conferir se está na lista')
strNumero = input()
strLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = iflista(strLista, strNumero)

print('')
print(result)
