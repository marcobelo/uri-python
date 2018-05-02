tempo = int(input())
segundos = int(tempo % 60)
tempo = tempo - segundos
horas = int(tempo / 3600)
tempo = tempo - (horas * 3600)
minutos = int(tempo / 60)
print('{}:{}:{}'.format(horas, minutos, segundos))
