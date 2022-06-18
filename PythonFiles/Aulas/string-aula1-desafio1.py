print('\nDigite a primeira string')
string1 = input()
print('\nDigite a segunda string')
string2 = input()

print(f'\nO tamanho da {string1} string é {len(string1)}')
print(f'O tamanho da {string2} string é {len(string2)}\n')

if (len(string1) != len(string2)):
    print('As duas strings possuem tamanhos diferentes\n'
          'As duas dtrings possuem conteúdos diferentes')
else:
    print('As stringd possuem o mesmo tamanho')
    if string1 == string2:
        print('As strings são iguais')
    else:
        print('As strings são diferentes')