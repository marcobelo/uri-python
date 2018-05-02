cedulas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]
valor = float(input())
i, d = divmod(valor, 1)
inteiro = int(i)
fracao = int(d * 100)
print('NOTAS:')
for cedula in cedulas:
    quantidade = int(inteiro / cedula)
    inteiro = inteiro % cedula
    print('{} nota(s) de R$ {:.2f}'.format(quantidade, cedula))
fracao = fracao + inteiro * 100
print('MOEDAS:')
for moeda in moedas:
    quantidade = int(fracao / moeda)
    fracao = fracao % moeda
    print('{} moeda(s) de R$ {:.2f}'.format(quantidade, moeda/100))
