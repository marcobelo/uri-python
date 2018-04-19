from math import sin, cos, sqrt


pi = 3.14159
g = 9.80665
altura_inicial = float(input())
p1, p2 = [int(num) for num in input().split(' ')]
tentativas = int(input())

for i in range(tentativas):
    ang, V = [float(num) for num in input().split(' ')]

    if ang == 90:
        Vx = 0
    else:
        Vx = V * abs(cos((ang*pi)/180))

    if ang == 0:
        Vy = 0
    else:
        Vy = V * abs(sin((ang*pi)/180))

    tempo_ar1 = (-Vy - sqrt((Vy*Vy) - 4*(-g/2)*altura_inicial))/(2*(-g/2))
    tempo_ar2 = (-Vy + sqrt((Vy*Vy) - 4*(-g/2)*altura_inicial))/(2*(-g/2))
    tempo_ar = max(tempo_ar1, tempo_ar2)

    dx = Vx * tempo_ar
    if p1 <= dx <= p2:
        print('{} -> DUCK'.format(round(dx, 5)))
    else:
        print('{} -> NUCK'.format(round(dx, 5)))
