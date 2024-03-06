#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

from math import hypot
oposto = float(input('Digite o valor do Cateto Oposto '))
adjacente = float(input('Digite o valor do cateto adjacente '))
hipotenusa = hypot(oposto,adjacente)
print('A Hipotenusa é: {:.2f}'.format(hipotenusa))

'''
#Minha solução:
from math import sqrt,pow
oposto = float(input('Digite o valor do cateto oposto '))
adjacente = float(input('Digite o valor do cateto adjacente'))
hipotenusa = sqrt((pow(oposto,2) + pow(adjacente,2)))
print('A hipotenusa do triangulo retangulo é {:.2f}'.format(hipotenusa))'''
