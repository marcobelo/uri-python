movimento = {'N': ['O', 'L'], 'L': ['N', 'S'], 'S': ['L', 'O'], 'O': ['S', 'N']}
while True:
    num_linhas, num_colunas, num_comandos = [int(x) for x in input().split()]

    if num_linhas == 0 and num_colunas == 0 and num_comandos == 0:
        break

    aux, direcao, matriz, direcoes = 0, '', [], ['N', 'S', 'O', 'L']
    pos_lin, pos_col, orientacao = None, None, None

    for lin_n in range(0, num_linhas):
        linha = input()
        if aux == 0 and any(direc in linha for direc in direcoes):
            pos_col = [linha.find(direc) for direc in direcoes]
            pos_lin = lin_n
            for num in range(0, len(pos_col)):
                if pos_col[num] != -1:
                    orientacao = direcoes[num]
                    pos_col = pos_col[num]
                    break
            aux = 1
        matriz.append(linha)

    instrucoes = input()
    pontuacao = 0

    for letra in instrucoes:
        if letra == 'D':
            orientacao = movimento[orientacao][1]
        elif letra == 'E':
            orientacao = movimento[orientacao][0]
        else:
            if orientacao == 'N' and pos_lin > 0:
                if matriz[pos_lin-1][pos_col] == '#':
                    pass
                else:
                    pos_lin -= 1
            elif orientacao == 'L' and pos_col < num_colunas-1:
                if matriz[pos_lin][pos_col+1] == '#':
                    pass
                else:
                    pos_col += 1
            elif orientacao == 'S' and pos_lin < num_linhas-1:
                if matriz[pos_lin+1][pos_col] == '#':
                    pass
                else:
                    pos_lin += 1
            elif orientacao == 'O' and pos_col > 0:
                if matriz[pos_lin][pos_col-1] == '#':
                    pass
                else:
                    pos_col -= 1

            if matriz[pos_lin][pos_col] == '*':
                pontuacao += 1
                i = pos_col
                matriz[pos_lin] = matriz[pos_lin][0:i] + '.' + matriz[pos_lin][i+1:]

    print(pontuacao)
