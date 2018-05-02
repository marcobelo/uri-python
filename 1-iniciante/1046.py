inicio, fim = [int(n) for n in input().split()]

if inicio > fim:
    tempo = 24 - inicio + fim
    print('O JOGO DUROU {} HORA(S)'.format(tempo))
elif inicio == fim:
    print('O JOGO DUROU 24 HORA(S)')
else:
    tempo = fim - inicio
    print('O JOGO DUROU {} HORA(S)'.format(tempo))
