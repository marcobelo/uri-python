num = [int(n) for n in input().split()]
num_sort = sorted(num)
if num_sort[1] % num_sort[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
