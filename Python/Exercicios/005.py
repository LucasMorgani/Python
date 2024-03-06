#Faça um programa que leia um numero inteiro e mostre seu sucessor e antecessor.

x = int(input('Digite um número inteiro'))
sucessor = x + 1
antecessor = x - 1

print('O número sucessor de {} é {}, e seu antecessor é {}.'.format(x,sucessor,antecessor))
