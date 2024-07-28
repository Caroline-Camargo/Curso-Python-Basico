# Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.

def calcular_consumo_medio(litros, distancia):
    consumo_medio = distancia / litros
    print(f'\nO consumo médio é de {consumo_medio:.2f} km/l')


print('--- Calculadora de consumo médio de combustível ---')
try:
    litros = float(input('\nPor favor, digite a quantidade de litros de combustível consumidos: '))
    distancia = float(input('Por favor, digite a distância percorrida: '))

except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')

else:
    if litros <= 0:
        print('Erro, a quantidade de litros de combustível consumidos não pode ser menor ou igual a zero')
    elif distancia <= 0:
        print('Erro, a distância percorrida não pode ser menor ou igual a zero')
    else:
        calcular_consumo_medio(litros, distancia)