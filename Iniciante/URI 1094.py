quantidade = int(input())
somaR = 0
somaC = 0
somaS = 0
for n in range(quantidade):
    quantia, tipo = input().split()
    quantia = int(quantia)
    if tipo == 'C':
        somaC += quantia
    elif tipo == 'R':
        somaR += quantia
    elif tipo == 'S':
        somaS += quantia
print(f'Total: {somaC + somaS + somaR} cobaias')
print(f'Total de coelhos: {somaC}')
print(f'Total de ratos: {somaR}')
print(f'Total de sapos: {somaS}')
print(f'Percentual de coelhos: {((somaC/(somaS + somaR + somaC)) * 100):.2f} %')
print(f'Percentual de ratos: {((somaR/(somaS + somaR + somaC)) * 100):.2f} %')
print(f'Percentual de sapos: {((somaS/(somaS + somaR + somaC)) * 100):.2f} %')