#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

x = float(input('Digite o salario para aplicar o aumento '))
aumento = x + (x * 0.15)

print('O seu salario era de R${} e com o aumento de 15% passou a ser de R%{}'.format(x,aumento))