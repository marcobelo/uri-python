from math import sqrt
p1 = [float(num) for num in input().split()]
p2 = [float(num) for num in input().split()]
aux = pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2)
distancia = sqrt(aux)
print('{0:.4f}'.format(distancia))
