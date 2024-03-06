#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qtde_dias = int(input('O carro foi alugado por quantos dias? '))
km = int(input('Digite a quantidade de km percorridos '))
preco = (qtde_dias * 60) + (km * 0.15)

print('Você deverá pagar R${}!'.format(preco))