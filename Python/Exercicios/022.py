#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiusculas
# - O nome com todas as letras minusculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo - ')).strip()
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
 

'''
#Minha solução:
import re
nome = str(input('Digite o seu nome completo ')).strip() #Removendo espaços nas extremidades do nome
print('Seu nome em letras maiusculas é - {}'.format(nome.upper()))
print('Seu nome em letras miudas é - {}'.format(nome.lower()))
#calculo de letras no nome total (sem espaços)
quantidade_letras_total = re.sub(r'\s+', '', nome)
print('A quantidade de caracteres do seu nome completo é : {}'.format(len(quantidade_letras_total)))
#calculo de letras do primeiro nome
print('O primeiro nome tem {} letras'.format(len(nome.split()[0])))
'''
