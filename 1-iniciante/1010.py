a = input().split(' ')
b = input().split(' ')
val_a = int(a[1]) * float(a[2])
val_b = int(b[1]) * float(b[2])
res = val_a + val_b
print("VALOR A PAGAR: R$ {0:.2f}".format(res))
