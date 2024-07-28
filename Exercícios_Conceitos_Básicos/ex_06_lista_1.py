'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

def calcular_tempo_viagem(distancia):
    tempo_aviao = distancia / 600
    tempo_carro = distancia / 100
    tempo_onibus = distancia / 80

    print(f'\nTempo de viagem:')
    print(f'Avião: {tempo_aviao:.2f} horas')
    print(f'Carro: {tempo_carro:.2f} horas')
    print(f'Ônibus: {tempo_onibus:.2f} horas')


print('--- Calculadora de tempo de viagem ---')
try:
    distancia = float(input('\nPor favor, digite a distância da viagem em km: '))

except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')

else:
    if distancia <= 0:
        print('Erro, a distância da viagem não pode ser negativa ou igual a zero')

    else:
        calcular_tempo_viagem(distancia)