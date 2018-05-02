reajustes = [15, 12, 10, 7, 4]
salario = float(input())
if salario <= 400.00:
    reajuste_perc = reajustes[0]
    reajuste = salario * (reajuste_perc/100)
elif salario > 400.00 and salario <= 800.00:
    reajuste_perc = reajustes[1]
    reajuste = salario * (reajuste_perc/100)
elif salario > 800.00 and salario <= 1200.00:
    reajuste_perc = reajustes[2]
    reajuste = salario * (reajuste_perc/100)
elif salario > 1200.00 and salario <= 2000.00:
    reajuste_perc = reajustes[3]
    reajuste = salario * (reajuste_perc/100)
elif salario > 2000.00:
    reajuste_perc = reajustes[4]
    reajuste = salario * (reajuste_perc/100)

novo_salario = salario + reajuste
print('Novo salario: {:.2f}'.format(novo_salario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(reajuste_perc))
