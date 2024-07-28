# Functions
'''
def function_name(parameters):
    code
    return value

function_name(arguments)
'''

def sum(num1, num2): # Defining a sum function 
    calc = num1 + num2
    print(f'The result sum is: {calc}')

def subtraction(num1, num2):  
    calc = num1 - num2
    print(f'The result subtraction is: {calc}')
    multiplication() # Calling the function inside another function

def multiplication(num1, num2):  
    calc = num1 * num2
    print(f'The result multiplication is: {calc}')

num1 = int(input('Type the first number: '))
num2 = int(input('Type the second number: '))

sum(num1, num2) # Calling the function 
subtraction(num1, num2) 
multiplication(num1, num2)
