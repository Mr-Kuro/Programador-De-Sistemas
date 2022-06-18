def verNum(numero):
    if '-' in numero:
        c = len(numero)
        if c == 10:
            return numero
        else:
            return '9' + numero
    else:
        c = len(numero)
        if c == 9:
            return numero
        else:
            return '9' + numero


print('\nDigite o número de telefone')
num = input()
scaneado = verNum(num)

print(scaneado)


# resolução do professor

print('\nDigite seu número de telefone')
telefone = input()

telefoneLimpo = telefone.replace('-', '')

if len(telefoneLimpo) == 8:
    print(f'opa fion, vou adiocionar o 9 na frente fo número\n'
          f'Telefone corrigido sem formatação 9{telefoneLimpo}')
    print(f'telefone corrigido com formatação: 9{telefone}')
