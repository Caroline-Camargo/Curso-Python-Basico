'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês.'''


def calcular_salario(horas_trabalhadas, valor_hora):
    salario = horas_trabalhadas * valor_hora
    print(f'\nO salário total no mês é de R$ {salario:.2f}')


print('--- Calculadora de salário mensal ---')
try:
    valor_hora = float(input('\nPor favor, digite quanto você ganha por hora: '))
    horas_trabalhadas = float(input('Por favor, digite o número de horas trabalhadas no mês: '))

except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')

else:
    if valor_hora < 0:
        print('Erro, o valor por hora não pode ser negativo')
    elif horas_trabalhadas <= 0:
        print('Erro, o número de horas trabalhadas no mês não pode ser negativo')
    else:
        calcular_salario(horas_trabalhadas, valor_hora)
