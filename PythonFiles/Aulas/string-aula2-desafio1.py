# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
# conte: quantos espaços em branco existem na frase. quantas vezes aparecem as vogais a, e, i, o, u.

def multi(vogal, espaco):
    return 0

print('\nDigite algo, minha fonte de renda.')
string = input()
string = string.lower()

a = 0
i = 0
u = 0
e = 0
o = 0
space = 0

for b in string:
    if b == 'a':
        a += 1
    elif b == 'i':
        i += 1
    elif b == 'u':
        u +=1
    elif b == 'e':
        e +=1
    elif b == 'o':
        o += 1
    elif b == ' ':
        space += 1
    else:
        pass
print(f'a - {a}\n'
      f'i - {i}\n'
      f'u - {u}\n'
      f'e - {e}\n'
      f'o - {o}\n'
      f'Soma - {a + i + u + e + o}\n'
      f"'  ' - {space}")

# Resolução do professor

print('\nDigite uma frase')
frase = input()
espacos = 0
vogais = 0

for i in frase:
    if 'AEIOU'.find(i.upper()) >= 0:
        vogais += 1
    elif i == ' ':
        espacos += 1
print(f'Espaços - {espacos}\n'
      f'Vogais  - {vogais}')
