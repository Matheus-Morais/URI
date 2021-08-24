pi = 3.14159
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
areaTriangulo = (A*C)/2
areaCirculo = ((C**2)*pi)
areaTrapezio = ((A+B)*C)/2
areaQuadrado = (B**2)
areaRetangulo = (A*B)
print(f'TRIANGULO: {areaTriangulo:.3f}\nCIRCULO: {areaCirculo:.3f}\nTRAPEZIO: {areaTrapezio:.3f}\nQUADRADO: {areaQuadrado:.3f}\nRETANGULO: {areaRetangulo:.3f}')