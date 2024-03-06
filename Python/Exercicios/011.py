#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la. Sabendo que cada litro de tinta pinta uma área de 2m^2.

alt = float(input('Digite a altura da sua parede '))
larg = float(input('Digite a largur da sua parede '))
metro_quad = alt * larg
litro_tinta = metro_quad / 2
print('Para pintar a sua parede, você precisará de {:.2f} litros de tinta'.format(litro_tinta))
