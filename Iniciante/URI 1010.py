codigo1, quantidade1, preco1 = input().split()
codigo2, quantidade2, preco2 = input().split()
quantidade1 = int(quantidade1)
quantidade2 = int(quantidade2)
preco1 = float(preco1)
preco2 = float(preco2)
total = ((quantidade1*preco1) + (quantidade2*preco2))
print(f'VALOR A PAGAR: R$ {total:.2f}')
