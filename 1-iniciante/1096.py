i, j = 1, 7
while True:
    print('I={} J={}'.format(i, j))
    if j == 5 and i == 9:
        break
    if j == 5:
        j = 7
        i += 2
    else:
        j -= 1
