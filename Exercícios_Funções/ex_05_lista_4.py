'''Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.'''

def contar_vogais(frase):
    vogais = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letra in frase:
        if letra.lower() in vogais:
            count += 1
    return count

print('--- Contador de vogais ---')
frase = input('Digite uma frase: ')
print(f'A frase tem {contar_vogais(frase)} vogais')
