produtos = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}
produto, quantidade = [int(num) for num in input().split()]
total = produtos[produto] * quantidade
print('Total: R$ {:.2f}'.format(total))
