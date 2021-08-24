renda = float(input())
if 0 <= renda <= 2000.00:
    mensagem = 'Isento'
elif 2000.01 <= renda <= 3000.00:
    imposto1 = (renda - 2000.00) * 0.08
    mensagem = f'R$ {imposto1:.2f}'
elif 3000.01 <= renda <= 4500.00:
    imposto2 = (renda - 3000) * 0.18
    mensagem = f'R$ {80 + imposto2:.2f}'
elif renda > 4500.01:
    imposto3 = (renda - 4500) * 0.28
    mensagem = f'R$ {350 + imposto3:.2f}'
print(mensagem)
