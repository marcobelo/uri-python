def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n-1)


a = int(input())
fatorial = fat(a)
print(fatorial)
