# adiciona as notas na lista e após printa a média

print('')

notas = []
soma = 0

for i in range(1, 5):
    print(f'Digite a nota {i}')
    notas.append(float(input()))

for i in notas:
    soma = soma + i  # ou soma = notas[i]

print(f' a soma é {soma / 4}')
