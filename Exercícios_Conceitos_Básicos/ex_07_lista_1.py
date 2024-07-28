'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''


classificacao_imc = {
    'abaixo do peso': 18.5,
    'peso normal': 24.9,
    'sobrepeso': 29.9,
    'obesidade grau 1': 34.9,
    'obesidade grau 2': 39.9,
    'obesidade extrema': 40
}

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f'\nSeu IMC é de {imc:.2f}')

    for key, value in classificacao_imc.items():
        if imc < value:
            print(f'Você está com {key}')
            break


print('--- Calculadora de IMC ---')
try:
    peso = float(input('\nPor favor, digite o peso em kg: '))
    altura = float(input('Por favor, digite a altura em metros: '))

except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')

else:
    if peso <= 0:
        print('Erro, o peso não pode ser menor ou igual a zero')
    elif altura <= 0:
        print('Erro, a altura não pode ser menor ou igual a zero')
    else:
        calcular_imc(peso, altura)