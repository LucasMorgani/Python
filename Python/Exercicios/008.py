#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

x = float(input('Digite um valor em metros '))
centimetro = x * 100
milimetros = centimetro * 10
print('"{}" metro são "{}" centimetros e "{}" milimetros'.format(x,centimetro,milimetros))