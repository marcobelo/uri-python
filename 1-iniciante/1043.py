abc = [float(n) for n in input().split()]
abc_sort = sorted(abc)

if (abc_sort[0] + abc_sort[1]) > abc_sort[2]:
    print('Perimetro = {:.1f}'.format(sum(abc_sort)))
else:
    area = ((abc[0]+abc[1])*abc[2]) / 2
    print('Area = {:.1f}'.format(area))
