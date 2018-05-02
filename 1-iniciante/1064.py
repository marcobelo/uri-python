total = 0
media = 0.0
for i in range(6):
    num = float(input())
    if num > 0.0:
        total += 1
        media += num
print('{} valores positivos'.format(total))
print('{:.1f}'.format(media/total))
