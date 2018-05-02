total = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        total += 1
print('{} valores pares'.format(total))
