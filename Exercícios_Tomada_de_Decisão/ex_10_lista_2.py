'''Faça um programa que lê três números inteiros e os mostra em ordem
crescente'''

print('----- Ordenação de Números -----')
num = []
try:
    num.append(int(input('Digite o primeiro número: ')))
    num.append(int(input('Digite o segundo número: ')))
    num.append(int(input('Digite o terceiro número: ')))
except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número inteiro')
else:
    num.sort()
    print(f'\nOs números em ordem crescente são: {num}')