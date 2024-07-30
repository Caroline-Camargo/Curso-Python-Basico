'''Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0'''

print('----- Média de Notas de Alunos -----')
QUANTIDADE_ALUNOS = 5
QUANTIDADE_NOTAS = 4

notasAlunos = []

for i in range(QUANTIDADE_ALUNOS):
    notas = []
    for j in range(QUANTIDADE_NOTAS):
        try:
            nota = float(input(f'Digite a nota {j+1} nota do aluno {i+1}: '))
        except:
            print('Erro, a entrada digitada é inválida! Por favor, digite um número')
            break
        else:
            notas.append(nota)
    else:
        notasAlunos.append(sum(notas)/QUANTIDADE_NOTAS)


print(notasAlunos)
print('\nAlunos com média maior ou igual a 7:')
aluno = 1
for nota in notasAlunos:
    if nota >= 7:
        print(f'Aluno {aluno}: {nota:.2f}')
    aluno += 1