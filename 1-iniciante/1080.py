maior = int(input())
pos = 1
for p in range(2, 101):
    num = int(input())
    if num > maior:
        maior = num
        pos = p
print(maior)
print(pos)
