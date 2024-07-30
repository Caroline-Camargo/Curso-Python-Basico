'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra'''

carrinho_compras = {}
total = 0

print('----- Carrinho de Compras -----')
while True:
    produto = input('Digite o nome do produto: ')

    try:
        quantidade = float(input('Digite a quantidade: '))
    except:
        print('Erro, a entrada digitada é inválida! Por favor, digite um número')
        break

    carrinho_compras[produto] = quantidade
    total += quantidade

    if input('Deseja adicionar mais produtos? (s/n): ').lower() == 'n':
        break


print('\n')
for produto, quantidade in carrinho_compras.items():
    print(f'{produto}: {quantidade}')
print(f'Total: {total:.2f}')