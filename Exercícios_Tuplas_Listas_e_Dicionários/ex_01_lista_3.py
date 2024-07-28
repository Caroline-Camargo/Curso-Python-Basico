'''Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário, ele será classificado como""Inocente"".'''


def verifica_se_resposta_eh_valida(resposta):
    if resposta in ['sim', 's', 'yes', 'y', '1']:
        return True
    elif resposta in ['não', 'nao', 'n', 'no', '0']:
        return False
    else:
        return None


def emitir_classificacao(respostas):
    if respostas.count(True) == 2: # Count retorna o número de ocorrências do item na lista
        print('\nSuspeita: Parece que você sabe mais do que está dizendo.')
    elif respostas.count(True) >= 3 and respostas.count(True) <= 4:
        print('\nCúmplice:  Seu envolvimento não é apenas uma coincidência.')
    elif respostas.count(True) == 5:
        print('\nAssassino: Todos os sinais indicam que você é o principal suspeito!')
    else:
        print('\nInocente: Você está livre de qualquer suspeita.')


perguntas = ['telefonou para a vítima?', 
             'esteve no local do crime?', 
             'mora perto da vítima?', 
             'devia para a vítima?', 
             'já trabalhou com a vítima?'
             ]
respostas = []


print('Por favor, responda o interrogatório a seguir:\n')
for pergunta in perguntas:
    resposta = None
    while resposta is None:
        resposta = input(f'Você {pergunta}\t').lower().strip()
        resposta = verifica_se_resposta_eh_valida(resposta)

        if resposta is None:
            print('Resposta inválida. Por favor, digite sim ou não.\n')
    respostas.append(resposta)

emitir_classificacao(respostas)
