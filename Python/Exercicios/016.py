#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

x = float(input('Digite um número Real e descubra o seu Inteiro '))
print('O número inteiro é {}'.format(math.floor(x))) #Arredonda o número para baixo
print('O número inteiro é {}'.format(math.trunc(x))) #Exclui tudo que tem depois da virgula do número

'''Outra resolução seria:
x = float(input('digite um número Real e descobra o seu Inteiro '))
print('O número inteiro é {}'.format(int(x)))'''
