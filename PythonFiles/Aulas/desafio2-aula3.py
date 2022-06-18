#Números entre 10 e 20
print('')
print('Números entre 10 e 20, ou diferentes dos números entre 10 e 20.')
print('Digite dez números consecutivos:')

contador = 10
num = 0
entreDezEVinte = 0
diferenteDeEntreDezEVinte = 0

for i in range(contador):
    num = int(input())
    if (num >= 10 and num <= 20):
        entreDezEVinte += 1
    elif (num < 10 or num > 20):
        diferenteDeEntreDezEVinte += 1
    else:
        print('Tá de onda?')

print(f'dentre os seus dez números digitados, {entreDezEVinte} estão entre dez e vinte')
print(f'dentre os seus dez números digitados, {diferenteDeEntreDezEVinte} estão diferentes dos números entre dez e vinte')
