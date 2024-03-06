#Faça um programa que leia um numero inteirp qualquer e mostre na tela a sua tabuada.

x = int(input('Digite um número inteiro e descubra a sua tabuada '))
x1 = x * 1
x2 = x * 2
x3 = x * 3
x4 = x * 4
x5 = x * 5
x6 = x * 6
x7 = x * 7
x8 = x * 8
x9 = x * 9
x10 = x * 10

print('A tabuada do {} é... '.format(x))
print('{} - {} - {}'.format(x1,x2,x3))
print('{} - {} - {}'.format(x4,x5,x6))
print('{} - {} - {}'.format(x7,x8,x9))
print('{:>5}'.format(x10))