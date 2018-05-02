testes = int(input())
for t in range(testes):
    a, b, c = [float(n) for n in input().split()]
    media = (a*2 + b*3 + c*5) / 10
    print('{:.1f}'.format(media))
