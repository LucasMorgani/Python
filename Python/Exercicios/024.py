#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

cidade = str(input('Digite o nome de uma cidade - ')).lower().strip()

if cidade.split()[0] == 'santo':
#if 'santo' in cidade.split()[0]: #Solução que falha
    print('Sim, sua cidade começa com SANTO!')
else:
    print('Não, sua cidade não começa com SANTO')
    
