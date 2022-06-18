import random


def jogoDados():
    jogada = random.randint(2, 12)
    return jogada


quantidadeJogadas = 1
ponto = 0

while True:
    jogada = jogoDados()
    print(f'jogada {quantidadeJogadas}: {jogada}')

    if quantidadeJogadas == 1:
        if(jogada == 2) or (jogada == 3) or (jogada == 12):
            print('Você perdeu')
            break
        elif jogada == 7:
            print('Você venceu')
            break
        else:
            ponto = jogada
            print(f'Seu ponto é: {ponto}')
    else:
        if jogada == 7:
            print('Você perdeu')
        elif jogada == ponto:
            print('Você venceu')
            break
    quantidadeJogadas += 1