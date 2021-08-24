dinheiro = int(input())
nota100 = dinheiro // 100
nota50 = (dinheiro - nota100*100) // 50
nota20 = (dinheiro - nota100*100 - nota50*50) // 20
nota10 = (dinheiro - nota100*100 - nota50*50 - nota20*20) // 10
nota5 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10) // 5
nota2 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5) // 2
nota1 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5 - nota2*2) // 1
print(f'{dinheiro}')
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')