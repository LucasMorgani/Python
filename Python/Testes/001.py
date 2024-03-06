n1 = int(input('Digite um número '))
n2 = int(input('Digite outro valor '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_real = n1 // n2
esponenciacao = n1 ** n2
print('O resultado das contas entre {} e {} é..'.format(n1, n2))
print('Soma = {}'.format(soma))
print('Multiplicação = {}'.format(multiplicacao))
print('Divisão = {:.2f}'.format(divisao), end=' / ') #:.2f(definindo que deve ter 3 casas flutuantes) / end=''(definindo a não quebra de linha)
print('Divisão inteira = {}'.format(divisao_real))
print('{}^{} = {}'.format(n1,n2,esponenciacao))




