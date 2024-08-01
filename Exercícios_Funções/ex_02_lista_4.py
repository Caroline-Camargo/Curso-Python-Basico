'''Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.'''

def reversoNumero(numero):
    numeroStr = str(numero)
    newNumero = ''
    for i in range(len(numeroStr)-1, -1, -1):
        newNumero += numeroStr[i]
    return int(newNumero)

try:
    numero = int(input('Digite um número inteiro: '))
except ValueError:
    print('Erro, a entrada digitada é inválida! Digite um número inteiro')
else:
    print(f'O reverso do número é {reversoNumero(numero)}')