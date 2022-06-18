#FATORIAL E UM NÚMERO QUALQUER
print('')
print('Digite o número para o fatorar')

# TÁ ERRADO

i = 0
factorial = 1
num = int(input())

if num < 0:
    print('não existe fatorial de números negativos')
elif num == 0:
    print('O fatorial de zero é 1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'O factorial é:{factorial}')
