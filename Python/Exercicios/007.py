#Um programa que leia as duas notas de um aluno. Calcule e mostre a sua média.

x1 = float(input('Digite a primeira nota do aluno '))
x2 = float(input('Digite a segunda nota do aluno '))

media = (x1 + x2) / 2

print('A média do aluno é de {:.1f} '.format(media))
