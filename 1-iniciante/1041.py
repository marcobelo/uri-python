x, y = [float(n) for n in input().split()]
if x == 0.0 and y == 0.0:
    print('Origem')
elif x > 0.0:
    if y == 0.0:
        print('Eixo X')
    elif y > 0.0:
        print('Q1')
    else:
        print('Q4')
elif x < 0.0:
    if y == 0.0:
        print('Eixo X')
    elif y > 0.0:
        print('Q2')
    else:
        print('Q3')
else:
    print('Eixo Y')
