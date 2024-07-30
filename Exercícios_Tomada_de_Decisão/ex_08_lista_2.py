'''Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.'''

print('----- Maior Número -----')
try:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    num3 = float(input('Digite o terceiro número: '))
except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')
else:
    if num1 > num2 and num1 > num3:
        print(f'O maior número é: {num1}')
    elif num2 > num1 and num2 > num3:
        print(f'O maior número é: {num2}')
    elif num3 > num1 and num3 > num2:
        print(f'O maior número é: {num3}')
    else:
        print('Os números são iguais')