''' Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.'''

print('----- Nome de Trás para Frente -----')
nome = input('Digite seu nome (pode digitar letras maiúsculas ou minúsculas): ').upper()

nomeInvertido = ''
for letra in range(len(nome)-1, -1, -1):
    nomeInvertido += nome[letra]
print(f'\nNome de trás para frente: {nomeInvertido}')