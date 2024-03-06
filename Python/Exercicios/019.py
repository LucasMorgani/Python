#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

from random import choice
aluno1 = input('Digite o nome do primeiro aluno ')
aluno2 = input('Digite o nome do segundo aluno ')
aluno3 = input('Digite o nome do terceiro aluno ')
aluno4 = input('Digite o nome do quarto aluno ')

print('O aluno sorteado foi o {}'.format(choice([aluno1,aluno2,aluno3,aluno4])))
