'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

aliquota = [0, 7.5/100, 15/100, 22.5/100, 27.5/100]

def calcular_salario_liquido(salario_bruto):
    if salario_bruto <= 1903.98:
        salario_liquido = salario_bruto
    elif salario_bruto <= 2826.65:
        salario_liquido = salario_bruto - (salario_bruto * aliquota[1])
    elif salario_bruto <= 3751.05:
        salario_liquido = salario_bruto - (salario_bruto * aliquota[2])
    elif salario_bruto <= 4664.68:
        salario_liquido = salario_bruto - (salario_bruto * aliquota[3])
    else:
        salario_liquido = salario_bruto - (salario_bruto * aliquota[4])

    print(f'\nO salário líquido é de R$ {salario_liquido:.2f}')


print('--- Calculadora de salário líquido ---')
try:
    salario_bruto = float(input('Digite o salário bruto: '))

except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número')

else:
    if salario_bruto < 0:
        print('Erro, o salário bruto não pode ser negativo')
    else:
        calcular_salario_liquido(salario_bruto)
