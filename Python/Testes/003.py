#From math import sqrt (para importar somente uma funcionalidade especifica)
import math
x = int(input('Digite um número: '))
raiz = math.sqrt(x)

print('A raiz de {} é {}'.format(x,math.floor(raiz))) #arredondando para baixo
print('A raiz de {} é {:.2f}'.format(x,math.ceil(raiz))) #arredondando para cima e com 2 casas decimais

'''quando utilizamos a importação especícica, não precisamos especifica-la novamente mais tar de. Ex:
raiz = sqrt(x) (baseado na linha 4)
ou
print('A raiz de {} é {}'.format(x,floor(raiz))) (baseado na linha 6)'''