test = 'this is just a short string'
test2 = 'KEK'
title = "This is a title"

print(test.find('s'))  # retorna em que posição está uma certa letra ou palavra procurada (o primeiro)
print(test.swapcase())  # troca tudo que é maiúsculo para minúsco e visce versa
print(test2.isupper())  # se é toda maiúscula
print(test.islower())  # se é toda minúscula

print(title.istitle())  # verifica se a primeira letra da palavra é maiúscula

print('    '.isspace())  # se uma string contém apenas espaços