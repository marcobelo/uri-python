i, j, des, aux = 0.0, 1.0, 0.0, 1.0
while True:
    ii, jj = round(i, 1), round(j, 1)
    if ii.is_integer():
        ii = int(ii)
    if jj.is_integer():
        jj = int(jj)
    print('I={} J={}'.format(ii, jj))
    if jj == 5 and ii == 2:
        break
    if aux == 3:
        des += 0.2
        aux = 1
        j = 1 + des
        i = des
    else:
        aux += 1
        j += 1
