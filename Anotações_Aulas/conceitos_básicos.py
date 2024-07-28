'''
Initial message 
to the 
user
'''

print('Hello World!') # This is a short comment
print('This is a first program in Python in the course of Python')


# Variables
# Type integer = int
number = int(input('Type your number: ')) #
print(f'The number typed is: {number}')

# Type float = float
number = float(input('\nType your float number: '))
print(f'The float number typed is: {number}')

# Type text = string
phrase = input('\nType your phrase: ')
print(f'The phrase typed is: {phrase}')


# Math operations
# Sum = +
number1 = int(input('\nType the first number: '))
number2 = int(input('Type the second number: '))
sum = number1 + number2
print(f'The sum of the numbers is: {sum}')

# Subtraction = -
number1 = int(input('\nType the first number: '))
number2 = int(input('Type the second number: '))
subtraction = number1 - number2
print(f'The subtraction of the numbers is: {subtraction}')

# Multiplication = *
number1 = int(input('\nType the first number: '))
number2 = int(input('Type the second number: '))
multiplication = number1 * number2
print(f'The multiplication of the numbers is: {multiplication}')

# Division = /
number1 = int(input('\nType the first number: '))
number2 = int(input('Type the second number: '))
division = number1 / number2
print(f'The division of the numbers is: {division}')

# Integer division = //
number1 = int(input('\nType the first number: '))
number2 = int(input('Type the second number: '))
integer_division = number1 // number2
print(f'The integer division of the numbers is: {integer_division}')


# Increment = +=
value = 5
value += 1
print(f'\nIncrement: {value}')

# Decrement = -=
value = 5
value -= 1
print(f'\nDecrement: {value}')

# Rest of Division = %
number1 = int(input('\nType the first number: '))
number2 = int(input('Type the second number: '))
rest = number1 % number2
print(f'The rest of division of the numbers is: {rest}')

# Order precedence = ()
calc = (5 + 3) * ((2 + 4) * 2)
print(f'\nResult: {calc}')


# Relacional operators
# == : Equal to 
# >  : Greater than
# >= : Greater than or equal to
# <  : Less than
# <= : Less than or equal to
# != : Different from


# f-strings
value = 45.3458372
print(f'{value:.2f}')
name = 'Caroline'
print(f'Hello {name}')

# str.format()
print('Hello {}, you are {} years old'.format('Caroline', 23))


