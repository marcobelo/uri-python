def fib(n, calc):
    if n == 0 or n == 1:
        if len(calc) < 2:
            calc.append(n)
        return calc[n], calc

    elif len(calc)-1 >= n:
        return calc[n], calc

    elif n >= 2:
        res1, c = fib(n-1, calc)
        res2, c = fib(n-2, calc)
        res = res1 + res2
        calc.append(res)
        return res, calc
    else:
        return calc[n], calc


a = int(input())
res = ''
calc = []
for num in range(0, a):
    n, calc = fib(num, calc)
    res += str(n) + ' '

print(res.strip())
