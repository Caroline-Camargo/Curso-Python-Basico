'''Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.'''

print('----- Classificação de Triângulos -----')
try:
    lado1 = float(input('Digite o comprimento do primeiro lado: '))
    lado2 = float(input('Digite o comprimento do segundo lado: '))
    lado3 = float(input('Digite o comprimento do terceiro lado: '))
except:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')
else:
    if lado1 == lado2 == lado3:
        print('O triângulo é equilátero!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo é isósceles!')
    else:
        print('O triângulo é escaleno!')
