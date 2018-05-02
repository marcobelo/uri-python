casos = '''10 C
6 R
15 S
5 C
14 R
9 C
6 R
8 S
5 C
14 R'''
cobaias = 0
coelhos = 0
ratos = 0
sapos = 0
entradas = int(input())
for ent in range(entradas):
    q, t = input().split()
    q = int(q)
    cobaias += q
    if t == 'C':
        coelhos += q
    elif t == 'R':
        ratos += q
    elif t == 'S':
        sapos += q
print('Total: {} cobaias'.format(cobaias))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format((coelhos/cobaias)*100))
print('Percentual de ratos: {:.2f} %'.format((ratos/cobaias)*100))
print('Percentual de sapos: {:.2f} %'.format((sapos/cobaias)*100))
