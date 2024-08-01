'''Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta'''


def celsiusParaFahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheitParaCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print('\n--- Conversor de temperatura ---')
    print('1 - Celsius para Fahrenheit')
    print('2 - Fahrenheit para Celsius')
    print('3 - Sair')
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Erro, a entrada digitada é inválida! Digite um número inteiro')
        return menu()
    return opcao

while True:
    opcao = menu()
    if opcao == 1:
        try:
            celsius = float(input('\nDigite a temperatura em Celsius: '))
        except ValueError:
            print('Erro, a entrada digitada é inválida! Digite um número')
        else:
            print(f'\nA temperatura em Fahrenheit é {celsiusParaFahrenheit(celsius)}')
    elif opcao == 2:
        try:
            fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        except ValueError:
            print('Erro, a entrada digitada é inválida! Digite um número')
        else:
            print(f'\nA temperatura em Celsius é {fahrenheitParaCelsius(fahrenheit)}')
    elif opcao == 3:
        break
    else:
        print('Opção inválida! Escolha uma opção válida')