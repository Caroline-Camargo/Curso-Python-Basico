'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''


print('----- Qual turno você estuda? -----')
turno = input(print('Digite: \nM - Matutino\nV - Vespertino\nN - Noturno')).upper()

if turno == 'M' or turno == 'MATUTINO':
    print('Bom dia!')
elif turno == 'V' or turno == 'VESPERTINO':
    print("Boa tarde!")
elif turno == 'N' or turno == 'NOTURNO':
    print("Boa noite!")
else:
    print("Valor inválido!")
