casos = int(input())
pares = [n for n in range(1, casos+1) if n % 2 == 0]
for n in pares:
    print('{}^2 = {}'.format(n, n*n))
