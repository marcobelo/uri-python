testes = int(input())
for tes in range(testes):
    n1, n2 = [int(n) for n in input().split()]
    numeros = [n for n in range((min(n1, n2))+1,(max(n1, n2))) if n % 2 != 0]
    print(sum(numeros))
