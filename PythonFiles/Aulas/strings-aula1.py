s = 'Olá, mundo!'
print('\n', len(s))  # tamanho
print('\n', s)

print('\nMeu Brasil ' + 'brasileiro')  # concatenação de string

s1 = s.replace('mundo', 'camarada')  # recolocar
print('\n', s1)
print(s.startswith('Olá'))  # começa com
print(f'\n', s1.count('camarada'))  # quantas ocorrencias da palavra camarada


# CAPTALIZAR
ss = 'joão Silva'
print('\n', ss.capitalize())  # Captalizar a primeira letra

print('\n12345'.isdigit())
print('\n12345abc'.isdigit())
print('\n12345abc*'.isalnum())  # verifica se é apenas número

ss = ' Olá, mundo!'
# usa-se em listas, tuplas e strings
print(ss[0])
print(ss[2])
print(ss[-1])
print(ss[0:-5])  # os números negativos sempre irão após os :(dois pontos)
print(ss[5:])  # irá do 5 até o final
print(ss[::-1])  # inverte as posicoes
print('u' in ss)
print(ss.lower())  # deixa todos os caracteres em ninusculo
print(ss.upper())  # deixa tudo maiúsculo
print(s.strip())  # corta os espaços iniciais e finas
print(','.join('abc'))  # separa usando delimitador indocado

