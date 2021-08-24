import math
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
delta = ((B ** 2) - (4 * A * C))
if delta < 0 or A == 0:
    print('Impossivel calcular')
else:
    bhaskara1 = (-B + math.sqrt(delta)) / (2 * A)
    bhaskara2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f'R1 = {bhaskara1:.5f}\nR2 = {bhaskara2:.5f}')