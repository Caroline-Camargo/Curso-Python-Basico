# Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return 'Não é possível dividir por zero'
    return n1 / n2


print('--- Calculadora de operações matemáticas ---')
try:
    n1 = float(input('\nPor favor, digite o primeiro número: '))
    n2 = float(input('Por favor, digite o segundo número: '))

except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')

else:
    print(f'\nSoma: {n1} + {n2} = {soma(n1, n2):.2f}')
    print(f'Subtração: {n1} - {n2} = {subtracao(n1, n2):.2f}')
    print(f'Multipliação: {n1} * {n2} = {multiplicacao(n1, n2):.2f}')
    print(f'Divisão: {n1} / {n2} = {divisao(n1, n2):.2f}')

