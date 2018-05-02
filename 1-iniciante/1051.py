salario = float(input())
imposto = [0.08, 0.18, 0.28]
if salario <= 2000.00:
    print('Isento')
else:
    devido = [0,0,0]
    if salario > 4500:
        devido[2] += devido[2] + (salario - 4500)
        devido[1] = 4500.0 - 3000.0
        devido[0] = 3000.0 - 2000.0
    elif salario > 3000 and salario <= 4500:
        devido[1] = salario - 3000.0
        devido[0] = 3000.0 - 2000.0
    else:
        devido[0] = salario - 2000.0
    pagar = devido[0]*imposto[0] + devido[1]*imposto[1] + devido[2]*imposto[2]
    print('R$ {:.2f}'.format(pagar))
