
carros = ['vector', 'Thor', 'mustang', 'scar', 'Versa']
consumo_de_gasolina_por_carro = []
contador = 0
menorC = 0

print('')
print('Digite quanto em lítros cada carro consome de gasolina')

for i in carros:
    print(f'{i}:')
    consumo_de_gasolina_por_carro.append(float(input()) / 1000)

for i in range(0, 5):
    print(carros[i])
    print(consumo_de_gasolina_por_carro[i])
    custo = consumo_de_gasolina_por_carro[i] * 2.5
    contador = contador + 1

#
# veiculos = []
# consumo = []
# preco = []
# menorConsumo = 0
#
# for i in range(1,6):
#     print('Digite o veiculo ', i)
#     veiculos.append(input())
#     print('Digite o Km por litro do veículo ', i)
#     consumo.append(float(input()))
#
# print('Relatoriofinal')
# for i in range(0,5):
#     custo = 1000/ consumo[i]
#     gasto = custo * preco
#     print("%d - %s - %.2f - %1f - litros - R$ %.2f" %\
#           (i + 1, veiculos [i], consumo [i], custo, gasto))
#     if menorConsumo > consumo[i]:
#         menorConsumo = i
#
# print("O menor consumo é do: ", veiculos[menorConsumo])