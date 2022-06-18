print('')
print('Este programa lhe permite criar uma lista  e manipulá-la.')
print('Digite os números:')

lista = []

for i in range(5):
    numeros = int(input())
    lista.append(numeros)

# comandos para as condições
print('')
print('° Vpara manipular a lista, observe a lista de comandos e após escreva o comando que quer executar.')
print('° Para remover um ítem da lista: ( remove )')
print('° Para limpar a lista: ( clear )')
print('° Para encontrar um ítem da lista: ( index )')
print('° Para saber quantos ítens semelhantes há na lista: ( count )')
print('° Para reordenar os ítens da lists em ordem crescente: ( sort )')
print('° Para reordenar os ítens da lists em ordem crescente: ( sort-reverse )')
print('° Para copiar a lista: ( copy )')
print('° Se não deseja fazer nada: ( pass )')

# só pra deixar o painel menos feio e ajudar quem tem "amnésia"
print('')
print(lista)
print('')

verify = ['remove', 'clear', 'index', 'count', 'sort', 'sort-reverse', 'copy', 'pass']  # lista com comandos executáveis
resposta = input()

# se  resposta estiver na verify, a verificação irá prosseguir com os 'if's. se não: Code developed by: ꧁Andy•🅺u͠r͠ø|黒꧂
if resposta in verify:
    print('')
    acao = verify.index(resposta)
    print(f'Lista: {lista}')
    print('')

    # verificação para remover ítens da lista
    if verify.index('remove') == acao:
        print('Digite a posição do ítem da lista deseja excluir. ( A contagem começa com 0)')
        excluir = int(input())
        excluido = lista.pop(excluir)
        if excluido in lista:
            print('')
            print(f'A reverificação diz que o ítem {excluido} não foi encontrado na lista.')
        else:
            print()
            print(f'O ítem {excluido} da posição {excluir} foi excluido da lista.')
            print(lista)
            print('')
            print(f'Ítem da posição {excluir} não está na lista.')
    # fim da verificação de remover ítems

    # verificação para limpar a lista
    elif acao == verify.index('clear'):
        lista.clear()
        print(f'todos os elemenentos da lista foram excluidos')
        print(f' {lista}')
    # fim da verificação para limpar a lista

    # verificação para encontrar a posição de um elemento da lista
    elif acao == verify.index('index'):
        print('Qual a posição do elemento da lista que deseja encontrar?')
        index = int(input())
        oIndex = lista.index(index)
        print('')
        if index in lista:
            print(f'O número {index} está na posição {oIndex} da lista.')
            print(lista)
        else:
            print(f'O número {index} não está na lista')
    #  fim da verificação para encontrar a posição de um elemento da lista

    # verificação para contar quantos números semelhantes há na lista
    elif acao == verify.index('count'):
        print('Digite o número que deseja procurar na lista:')
        count = int(input())
        counter = lista.count(count)
        print('')
        print(f' Há {counter} números {count} na lista')
    # fim da verificação para contar quantos números semelhantes há na lista

    # verificação para por os itens da lista em ordem crescente
    elif acao == verify.index('sort'):
        lista.sort()
        print(f'A lista foi reordenada para {lista}')
    # fim da verificação para por os itens da lista em ordem crescente

    # verificação para por os itens da lista em ordem decrescente
    elif acao == verify.index('sort-reverse'):
        reSort = lista.sort(reverse=True)
        print(f'A lista foi reordenada para {lista}')
    # dim da verificação para por os itens da lista em ordem decrescente

    # verificação para copiar a lista
    elif acao == verify.index('copy'):
        copia = lista.copy()
        print(f'A lista {lista} foi copiada: {copia}')
    # fim da verificação para copiar a lista

    # verificação para não fazer nada
    elif acao == verify.index('pass'):
        pass
    # verificação para não fazer nada

else:
    print('Code developed by: ꧁Andy•🅺u͠r͠ø|黒꧂')
