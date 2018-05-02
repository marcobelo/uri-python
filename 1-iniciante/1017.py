rendimento = 12  # km/l
tempo = int(input())
velocidade = int(input())
distancia = velocidade * tempo
consumo = distancia / rendimento
print('{:.3f}'.format(consumo))
