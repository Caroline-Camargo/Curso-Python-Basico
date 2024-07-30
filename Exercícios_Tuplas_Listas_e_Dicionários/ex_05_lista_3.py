# Crie duas tuplas. Concatene-as para formar uma nova tupla.

print('----- Concatenando tuplas -----')
tupla1 = ()
tupla2 = ()

tupla1 = tuple(input('Digite os elementos da primeira tupla separados por espaço: ').split())
tupla2 = tuple(input('Digite os elementos da segunda tupla separados por espaço: ').split())

tupla3 = tupla1 + tupla2
print(f'Tupla concatenada: {tupla3}')

