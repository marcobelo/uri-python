cedulas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())
print(valor)
for cedula in cedulas:
    quantidade = int(valor / cedula)
    valor = valor % cedula
    print('{} nota(s) de R$ {},00'.format(quantidade, cedula))
