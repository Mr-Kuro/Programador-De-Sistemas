#Valo do pagamento com taxa e juros

def valor_pagamento(custo, atraso):
    taxaDeAtraso = custo * (atraso * 1 / 100)
    if taxaDeAtraso != 0:
        multa = custo + (custo * 3 / 100)
        valorDoPagamento = multa + taxaDeAtraso
    else:
        valorDoPagamento = custo
    return valorDoPagamento


counter = 1
prestacoesPagasHoje = -1
valorTotalDePrestacoesPagasHoje = 0
while counter > 0:
    print('\nDigite o custo do produto:')
    strCusto = float(input())
    counter = strCusto
    print('\nDigite os dias de atraso do pagamento da parcela:')
    strAtraso = float(input())

    result = valor_pagamento(strCusto, strAtraso)

    prestacoesPagasHoje += 1
    valorTotalDePrestacoesPagasHoje +=+ result

    if counter == 0:
        print(f'\nQuantidades de prestações pagas hoje - {prestacoesPagasHoje}\n'
              f'Valor total de prestações pagas hoje - R${valorTotalDePrestacoesPagasHoje:.2f}')
    else:
        print(f'\nO valor total do produto + 3% multa por atraso + 1% taxa de atraso/dia é: R${result:.2f}')
        print('\n[Digite o número zero para encerrar o programa!]')
