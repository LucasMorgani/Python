#Faça um algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto.

x = float(input('Digite o preço do produto para aplicar o desconto '))
desc = x - (x * 0.05)
print('R${:.2f} com 5% de desconto é R${:.2f}'.format(x,desc))