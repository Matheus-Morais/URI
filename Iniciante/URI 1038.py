codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)
if codigo == 1:
    preco = quantidade * 4
elif codigo == 2:
    preco = quantidade * 4.5
elif codigo == 3:
    preco = quantidade * 5
elif codigo == 4:
    preco = quantidade * 2
elif codigo == 5:
    preco = quantidade * 1.5
print(f'Total: R$ {preco:.2f}')
