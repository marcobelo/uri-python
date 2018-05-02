casos = int(input())
dentro = 0
fora = 0
for i in range(casos):
    num = int(input())
    if num >= 10 and num <= 20:
        dentro += 1
    else:
        fora += 1
print('{} in\n{} out'.format(dentro, fora))
