#Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
aluno1 = input('Digite o nome do primeiro aluno ')
aluno2 = input('Digite o nome do segundo aluno ')
aluno3 = input('Digite o nome do terceiro aluno ')
aluno4 = input('Digite o nome do quarto aluno ')
lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print('A Ordem de apresentação é')
print(lista)

'''
Minha solução -
from random import sample
aluno1 = input('Digite o nome do primeiro aluno ')
aluno2 = input('Digite o nome do segundo aluno ')
aluno3 = input('Digite o nome do terceiro aluno ')
aluno4 = input('Digite o nome do quarto aluno ')

print('O sorteio dos alunos foi', sample([aluno1,aluno2,aluno3,aluno4], k=4))
'''