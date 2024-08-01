'''Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício'''

import random
TENTATIVAS = 6
palavras_secretas = []

def importar_arquivo():
    try:
        arquivo = open('Exercícios_Funções\esportes_olimpiadas.txt', 'r')
    except FileNotFoundError:
        print('Erro! Arquivo não encontrado')
    else:
        for linha in arquivo:
            palavras_secretas.append(linha.strip())

def sortear_palavra():
    return random.choice(palavras_secretas)

def inicializar_palavra_secreta(palavra):
    palavra_secreta = ''
    for letra in palavra:
        if letra == ' ':
            palavra_secreta += ' '
        else:
            palavra_secreta += '_'
    return palavra_secreta

def atualizar_palavra_secreta(palavra_secreta, palavra_escolhida, letra):
    for i in range(len(palavra_escolhida)):
        if palavra_escolhida[i] == letra:
            palavra_secreta = palavra_secreta[:i] + letra + palavra_secreta[i + 1:]
    return palavra_secreta

def testa_vitoria(palavra_secreta, palavra_escolhida):
    if palavra_secreta.lower() == palavra_escolhida.lower():
        print('Parabéns, você venceu!')
        return True
    else:
        return False

def jogar():
    tentativas = 0
    letras_erradas = []
    letras_corretas = []
    palavra_escolhida = sortear_palavra().lower()
    palavra_secreta = inicializar_palavra_secreta(palavra_escolhida)
    print(palavra_secreta)

    while tentativas < TENTATIVAS:
        print('\n\n\n\n--- Jogo da forca ---')
        print(f'Letras erradas: {letras_erradas}')
        print(f'Tentativas restantes: {TENTATIVAS - tentativas}')
        print(f'Palavra: {palavra_secreta}\n\n')

        letra = input('Digite uma letra: ')
        if letra.lower() not in letras_corretas and letra.lower() in palavra_escolhida.lower():
            palavra_secreta = atualizar_palavra_secreta(palavra_secreta, palavra_escolhida, letra)
            print('Letra encontrada!')
        else:
            print('Letra não encontrada!')
            if letra.lower() in letras_erradas:
                print('Você já tentou essa letra!')
            else:
                tentativas += 1
                letras_erradas.append(letra.lower())

        if testa_vitoria(palavra_secreta, palavra_escolhida):
            break

        if tentativas == TENTATIVAS:
            print('\n\nVocê perdeu! A palavra secreta era:', palavra_escolhida)

importar_arquivo()

while True:
    jogar()
    continuar = input('Deseja jogar novamente? (s/n): ')
    if continuar.lower() != 's':
        break



