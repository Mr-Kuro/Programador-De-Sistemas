# MENOR OU IGUAL
def menorIgual(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if num1 > num2:
        resultado = f'{num1} é maior que {num2}'
    elif num1 < num2:
        resultado = f'{num2} é maior que {num1}'
    else:
        resultado = f'{num1} e {num2} possuem o mesmo valor'
    return resultado

print('')
print('Digite o primeiro número')
strNum1 = input()
print('Digite o segundo número')
strNum2 = input()

menor_igual = menorIgual(strNum1, strNum2)
print(menor_igual)