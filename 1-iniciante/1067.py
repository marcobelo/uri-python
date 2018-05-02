num = int(input())
pares = [n for n in range(1,num+1) if n % 2 != 0]
for n in pares:
    print(n)
