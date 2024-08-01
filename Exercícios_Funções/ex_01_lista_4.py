'''Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos'''

def soma(a, b, c):
    return a + b + c

try:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    c = float(input('Digite o terceiro número: '))
except ValueError:
    print('Erro, a entrada digitada é inválida! Digite um número')
else:
    print(f'A soma dos números é {soma(a, b, c)}')