'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício'''


def calcular_calorias_queimadas(horas):
    calorias_queimadas = 5 * 60 * horas * 4 # 4 semanas em um mês, X horas por semana, 60 minutos por hora, 5 calorias por minuto
    print(f'\nVocê queimou {calorias_queimadas} calorias em um mês')


print('--- Calculadora de calorias queimadas ---')
try:
    horas = float(input('\nPor favor, digite o número de horas de exercício físico por semana: '))

except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')
    
else:
    if horas < 0:
        print('Erro, o número de horas de exercício físico por semana não pode ser negativo')
    else:
        calcular_calorias_queimadas(horas)
