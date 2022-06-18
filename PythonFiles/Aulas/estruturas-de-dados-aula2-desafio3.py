
perguntas = ['Você telefonou para a vítima?',
             'Você esteve no local do crime?',
             'Vôce mora perto da vítima?',
             'você trabalhou para a vítima?']

respostas = []

for i in perguntas:
    print(i)
    respostas.append(input())

classificacao = 0
for i in respostas:
    if i == 'sim':
        classificacao += 1

if classificacao > 2:
    print("Inocente")
elif classificacao == 2:
    print('Suspeito')
elif classificacao >= 4:
    print('Cumplice')
else:
    print("ASSASSINOOO!")