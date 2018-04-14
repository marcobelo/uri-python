pi = 3.14159
a = [float(x) for x in input().split()]
res1 = (a[0]*a[2])/2
res2 = pi*pow(a[2], 2)
res3 = ((a[0]+a[1])*a[2])/2
res4 = a[1] * a[1]
res5 = a[0] * a[1]
print("TRIANGULO: {0:.3f}".format(res1))
print("CIRCULO: {0:.3f}".format(res2))
print("TRAPEZIO: {0:.3f}".format(res3))
print("QUADRADO: {0:.3f}".format(res4))
print("RETANGULO: {0:.3f}".format(res5))
