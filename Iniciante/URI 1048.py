salario = float(input())
if 0 <= salario <= 400.00:
    porcentagem = 15
    reajuste = salario * (porcentagem / 100)
    novoSalario = salario + reajuste
elif 400.01 <= salario <= 800.00:
    porcentagem = 12
    reajuste = salario * (porcentagem / 100)
    novoSalario = salario + reajuste
elif 800.01 <= salario <= 1200.00:
    porcentagem = 10
    reajuste = salario * (porcentagem / 100)
    novoSalario = salario + reajuste
elif 1200.01 <= salario <= 2000.00:
    porcentagem = 7
    reajuste = salario * (porcentagem / 100)
    novoSalario = salario + reajuste
elif salario > 2000.00:
    porcentagem = 4
    reajuste = salario * (porcentagem / 100)
    novoSalario = salario + reajuste
print(f'Novo salario: {novoSalario:.2f}'
      f'\nReajuste ganho: {reajuste:.2f}'
      f'\nEm percentual: {porcentagem} %')