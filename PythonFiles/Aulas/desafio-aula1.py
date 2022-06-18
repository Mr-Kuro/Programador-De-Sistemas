# PROGRAMA PARA CAUCULA POTÊNCIA
print('')

print('Digite a base')
base = int(input())
print('Dighite o expoente')
expoente = int(input())

result = base

# for i in range(expoente - 1):
#     result = base * result
# print(result)

while expoente > 1:
    result = base * result
    expoente = expoente - 1
print(result)
