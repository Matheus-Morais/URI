nota1, nota2, nota3, nota4 = input().split()
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
media = ((nota1*2) + (nota2*3) + (nota3*4) + nota4) / 10
print(f'Media: {media:.1f}')
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    notaExame = float(input())
    print(f'Nota do exame: {notaExame:.1f}')
    novaMedia = (media + notaExame) / 2
    if novaMedia >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {novaMedia}')
    elif novaMedia <= 4.9:
        print('Aluno reprovado.')
        print(f'Media final: {novaMedia}')