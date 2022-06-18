#REAJUSTE SALÁRIAL:
print('')

print('Digite o seu Salário')
salario = float(input())

# CONDIÇÕES PARA O REAJUSTE
if salario <= 500:
    reajuste = (salario * 15) / 100
    novoSalario = salario + reajuste
elif salario <= 1000:
    reajuste = (salario * 10) / 100
    novoSalario = salario + reajuste
else:
    reajuste = (salario * 5) / 100
    novoSalario = salario + reajuste
# FIM DAS CONDIÇÕES

print(f'Seu novo salário é: {novoSalario}')
