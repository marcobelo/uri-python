num = float(input())
if num < 0.0 or num > 100.0:
    print('Fora de intervalo')
elif num <= 25.0:
    print('Intervalo [0,25]')
elif num <= 50.0:
    print('Intervalo (25,50]')
elif num <= 75.0:
    print('Intervalo (50,75]')
elif num <= 100.0:
    print('Intervalo (75,100]')
