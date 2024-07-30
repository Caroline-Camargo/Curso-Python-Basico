'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''

print('----- Contagem de Números Pares e Ímpares -----')

numPares = 0
numImpares = 0


while True:
    numDigitado = -1
    try:
        numDigitado = int(input('Digite um número inteiro positivo: '))
    except ValueError:
        print('Erro, a entrada digitada é inválida! Por favor, digite um número inteiro')
    else:
        if numDigitado < 0:
            print('Erro, o número digitado é inválido! Por favor, digite um número positivo')
        elif numDigitado == 0:
            break
        elif numDigitado % 2 == 0:
            numPares += 1
        else:
            numImpares += 1
    
print(f'\nQuantidade de números pares: {numPares}')
print(f'\nQuantidade de números ímpares: {numImpares}')
