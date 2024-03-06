#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome

nome = str(input('Digite o seu nome completo - ')).lower().strip()

if 'silva' in nome:
    print('Você tem SILVA no nome!')
else:
    print('Você não tem SILVA no nome!')