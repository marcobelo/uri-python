hi, mi, hf, mf = [int(n) for n in input().split()]

if hi == hf and mi == mf:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    if hi > hf:
        horas = 24 - hi + hf
    else:
        horas = hf - hi
    if mi < mf:
        minutos = mf - mi
    elif mi > mf:
        minutos = 60 - mi + mf
        horas = horas - 1
    else:
        minutos = 0
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
