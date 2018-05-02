A, B, C = [float(num) for num in input().split()]
delta = pow(B, 2) - 4*A*C
if delta < 0.0 or A == 0.0:
    print('Impossivel calcular')
else:
    delta_sqrt = pow(delta, 0.5)
    r1 = (-B + delta_sqrt)/(2*A)
    r2 = (-B - delta_sqrt)/(2*A)
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(r1, r2))
