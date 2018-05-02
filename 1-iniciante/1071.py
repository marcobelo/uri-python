n1 = int(input())
n2 = int(input())
numeros = [n for n in range((min(n1, n2))+1,(max(n1, n2))) if n % 2 != 0]
print(sum(numeros))
