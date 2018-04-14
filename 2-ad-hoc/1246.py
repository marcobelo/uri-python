while True:
    try:
        comprimento, eventos = [int(x) for x in input().split()]
    except EOFError:
        break
    lucro, utilizado, estacionamento = 0, 0, {}  # 'veic' : tamanho
    for aux in range(0, eventos):
        evento = input().split(' ')
        if len(evento) == 3:  # entrada veic
            if comprimento >= (utilizado + int(evento[2])):
                # ok estacionar
                utilizado += int(evento[2])
                estacionamento[evento[1]] = int(evento[2])
                lucro += 10
        elif len(evento) == 2:  # saida veic
            try:
                veic_tam = estacionamento[evento[1]]
            except:
                veic_tam = 0
            utilizado -= veic_tam
    print(lucro)
