i, j, des = 1, 7, 0
while True:
    print('I={} J={}'.format(i, j))
    if j == 5 + des and i == 9:
        break
    if j == 5 + des:
        des += 2
        j = 7 + des
        i += 2
    else:
        j -= 1
