# quantos são maiores que o parâmetro

def maiorais(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a or b > c:
        print(f'apenas 1 dos parâmetros é maior que {c}')
    elif a and b > c:
        print(f'os Dois parâmetros são maiores que {c}')
    else:
        print(f'Nenhum dos parâmetros é maior que {c}')

print('')
print('Digite o primeiro parâmetro:')
strA = input()
print('Digite o segundo parâmetro')
strB = input()
print('Digite o limitador')
strC = input()

marmininu = maiorais(strA, strB, strC)
print(marmininu)
print('')
print('Acabou! isso aqui né parquinho não.')
