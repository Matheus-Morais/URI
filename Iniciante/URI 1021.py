dinheiro = float(input())
nota100 = dinheiro // 100
nota50 = (dinheiro - nota100*100) // 50
nota20 = (dinheiro - nota100*100 - nota50*50) // 20
nota10 = (dinheiro - nota100*100 - nota50*50 - nota20*20) // 10
nota5 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10) // 5
nota2 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5) // 2
moeda100 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5 - nota2*2) // 1
moeda50 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5 - nota2*2 - moeda100) // 0.5
moeda25 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5 - nota2*2 - moeda100 - moeda50*0.5) // 0.25
moeda10 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5 - nota2*2 - moeda100 - moeda50*0.5 - moeda25*0.25) // 0.10
moeda5 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5 - nota2*2 - moeda100 - moeda50*0.5 - moeda25*0.25 - moeda10*0.10) // 0.05
moeda1 = (dinheiro - nota100*100 - nota50*50 - nota20*20 - nota10*10 - nota5*5 - nota2*2 - moeda100 - moeda50*0.5 - moeda25*0.25 - moeda10*0.10 - moeda5*0.05) // 0.01
print('NOTAS:')
print(f'{nota100:.0f} nota(s) de R$ 100.00')
print(f'{nota50:.0f} nota(s) de R$ 50.00')
print(f'{nota20:.0f} nota(s) de R$ 20.00')
print(f'{nota10:.0f} nota(s) de R$ 10.00')
print(f'{nota5:.0f} nota(s) de R$ 5.00')
print(f'{nota2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda100:.0f} moeda(s) de R$ 1.00')
print(f'{moeda50:.0f} moeda(s) de R$ 0.50')
print(f'{moeda25:.0f} moeda(s) de R$ 0.25')
print(f'{moeda10:.0f} moeda(s) de R$ 0.10')
print(f'{moeda5:.0f} moeda(s) de R$ 0.05')
print(f'{moeda1:.0f} moeda(s) de R$ 0.01')
