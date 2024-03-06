#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: número 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1


#Versão por inteiro
numero = int(input('Digite um numero de 0 a 9999 - '))

# Extrair os dígitos
#unidade
unidade = numero % 10
#dezena
numero = numero // 10 #183
dezena = numero % 10
#centena
numero = numero // 10 #18
centena = numero % 10
#milhar
numero = numero // 10 #1
milhar = numero % 10 #como 1 é menor que 10, o retorno será o proprio número (1)

# Imprimir os resultados
print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)

'''
#Versão por string
numero = str(input('Digite um numero de 0 a 9999 - '))
numero = numero[::-1]
caracteres = list(numero)
print('A unidade é {}'.format(caracteres[0]))
print('A dezena é {}'.format(caracteres[1]))
print('A centena é {}'.format(caracteres[2]))
print('A milhar é {}'.format(caracteres[3]))
'''
