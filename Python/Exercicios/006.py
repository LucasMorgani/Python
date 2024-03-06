#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

x = int(input('Digite um número '))
dobro = x * 2
triplo = x * 3
raiz = x ** 0.5

print('O número digitado foi {}.'.format(x))
print('O DOBRO deste número é {}'.format(dobro))
print('O TRIPLO deste número é {}'.format(triplo))
print('A RAIZ QUADRADA deste número é {}'.format(raiz))