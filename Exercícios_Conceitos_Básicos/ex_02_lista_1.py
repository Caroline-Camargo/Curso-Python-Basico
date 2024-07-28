# Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

def calcular_idade(ano_nascimento):
    idade = 2024 - ano_nascimento
    print(f'\nVocê tem {idade} anos')


print('--- Calculadora de idade ---')
try:
    ano_nascimento = int(input('\nPor favor, digite o ano de nascimento: '))
except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')
else:
    if ano_nascimento > 2024:
        print('Erro, o ano de nascimento não pode ser maior que o ano atual')
    elif ano_nascimento < 0:
        print('Erro, o ano de nascimento não pode ser negativo')
    else:
        calcular_idade(ano_nascimento)
