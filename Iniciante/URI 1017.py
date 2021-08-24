tempoViagem= int(input())
velocidadeMedia = int(input())
consumoMedio = 12
combustivelNecessario = (velocidadeMedia*tempoViagem)/consumoMedio
print(f'{combustivelNecessario:.3f}')
