#calcular valor de horas trabalhadas

salario = float(input('Digite seu salario '))
horas_dia = int(input('Digite a sua carga horaria por dia '))
dias_mes = int(input('Digite quantos dias uteis tem o mes '))

calcular_hora = (salario / dias_mes) / horas_dia
calcular_dia = salario / dias_mes

print('O valor da sua hora trabalhada é: {:.2f}'.format(calcular_hora))
print('O valor do seu dia trabalhado é: {:.2f}'.format(calcular_dia))