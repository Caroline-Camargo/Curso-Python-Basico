'''Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.'''

print('----- Classificação de Idade -----')
try:
    idade = int(input('Digite a idade: '))
except:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número inteiro')
else:
    if idade < 0:
        print('Erro, a idade não pode ser negativa!')
    elif idade < 12:
        print('Criança')
    elif idade < 18:
        print('Adolescente')
    elif idade < 60:
        print('Adulto')
    elif idade < 120:
        print('Idoso')
    else:
        print('Erro, a idade não pode ser maior que 120 anos!')