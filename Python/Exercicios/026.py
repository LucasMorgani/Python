#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'a'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase - ')).lower().strip()

print('A letra "a" aparece {} vezes!'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na {}° posição!'.format(frase.find('a') + 1))
print('A letra "a" aparece pela ultima vez na {}° posição!'.format(frase.rfind('a') + 1))
