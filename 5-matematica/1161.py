def fat(fatoriais, maior):
    for num in range(len(fatoriais), maior+1):
        fatoriais.append(num * fatoriais[-1])
    return fatoriais


def sum_fat(a, b):
    maior = max(a, b)
    fatoriais = [1, 1, 2]
    if maior > 2:
        fatoriais = fat(fatoriais, maior)
    return fatoriais[a] + fatoriais[b]


while True:
    try:
        a, b = [int(num) for num in input().split(' ')]
    except (ValueError, EOFError):
        break
    print(sum_fat(a, b))
