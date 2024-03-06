# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# considere o dolar em US$1.00 = R$3.27

x = float(input('Digite quantos Reais você tem '))
dolar = x / 3.27
print('Com R${} você consegue comprar US${:.2f} '.format(x, dolar))
