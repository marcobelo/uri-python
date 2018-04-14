def maiorAB(a, b):
    return (a + b + abs(a-b))/2


numeros = input().split()
maior_temp = maiorAB(int(numeros[0]), int(numeros[1]))
maior = maiorAB(maior_temp, int(numeros[2]))

print('{} eh o maior'.format(int(maior)))
