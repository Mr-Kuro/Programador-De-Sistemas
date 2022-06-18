def somaImposto(taxaImposto, custo):
    taxaImposto = float(taxaImposto)
    custo = float(custo)
    novoCusto = custo + (custo * taxaImposto / 100)
    return novoCusto


print('')
print("Digite o custo do produto:")
strCusto = input()
print('Digite o imposto incidente sobre o produto em R$:')
strImposto = input()

retorno = somaImposto(strImposto, strCusto)
print(f'{retorno:.2f}')
