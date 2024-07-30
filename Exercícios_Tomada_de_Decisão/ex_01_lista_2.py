# Faça um Programa que peça dois números e imprima o maior deles.

try:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')
else:
    if num1 > num2:
        print(f'O maior número é: {num1}')
    elif num1 < num2:
        print(f'O maior número é: {num2}')
    else:
        print('Os números são iguais')
        