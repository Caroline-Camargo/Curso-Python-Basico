'''Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.'''

contatos = {}

def adicionar_contato():
    nome = input('\nDigite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    contatos[nome] = telefone


def procurar_contato():
    nome = input('\nDigite o nome do contato que deseja procurar: ')
    if nome in contatos.keys():
        print(f'{nome}: {contatos[nome]}')
    else:
        print('Contato não encontrado')

def listar_contatos():
    print('\nLista de contatos:')
    for nome, telefone in contatos.items():
        print(f'{nome}: {telefone}')

while True:
    print('\n----- Agenda de Contatos -----')
    print('1 - Adicionar contato')
    print('2 - Procurar contato')
    print('3 - Sair')

    try:
        opcao = int(input('Digite a opção desejada: '))
    except:
        print('Erro, a entrada digitada é inválida! Por favor, digite um número')
    else:
        if opcao == 1:
            adicionar_contato()
        elif opcao == 2:
            procurar_contato()
        elif opcao == 3:
            break
        else:
            print('Opção inválida')