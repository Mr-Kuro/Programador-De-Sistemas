#ESTRUTURAS DE REPETIÇÃO E ESTRUTURAS CONDICIONAIS
# c = 1
# while c < 5:
#     print('Digite a nota')
#     m = float(input())
#     m = m + m
#     c = c + 1
#
# m = m/4
# if m >= 7:
#     print('aprovado')
# elif m >= 5:
#     print('recuperação')
# else:
#     print('reprovado')

c = 4
i = 0
for i in range(c):
    print('Digite a nota ')
    m = float(input())
    m = m + m

m = m / 4
if m >= 7:
    print('aprovado') #range = altura
elif m >= 5:
    print('reciperação')
else:
    print('reprovado')
print(f'sua média é {m}.')
# (for [variável] in(em) range [variável]
# também poderia ser:
for i in range(4):
    print(i)
    n = n + int(input())
