num = int(input())
pares = [n for n in range(1,10001) if n % num == 2]
for n in pares:
    print(n)
