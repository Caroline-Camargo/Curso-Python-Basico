'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.'''

nota = -1
while nota < 0 or nota > 10:
    try:
        nota = float(input('\nPor favor, digite uma nota entre 0 e 10: '))
    except ValueError:
        print('Erro, a entrada digitada é inválida! Por favor, digite um número')
    else:
        if nota < 0:
            print('Erro, a nota digitada é inválida! Por favor, digite uma nota positiva')
        elif nota > 10:
            print('Erro, a nota digitada é inválida! Por favor, digite uma nota menor ou igual a 10')
        else:
            print(f'A nota digitada foi: {nota}')
            break
