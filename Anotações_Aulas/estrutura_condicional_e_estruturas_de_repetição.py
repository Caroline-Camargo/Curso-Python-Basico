# Relacional operators
# == : Equal to 
# >  : Greater than
# >= : Greater than or equal to
# <  : Less than
# <= : Less than or equal to
# != : Different from


# Conditional structure
'''
if condition:
     code
 else:
     code
'''

number = int(input('Type the number: '))
if number > 0:
    print('The number is positive')
else:
    print('The number is negative')


# Repetition structure
'''
while condition:
    code
    increment
'''

number = -1
while number < 0: # 
    number = int(input('Type the number: '))
print('The positive number was entered successfully')


'''
for variable in range(start, end, increment):
    code
'''
fruits = ['apple', 'banana', 'grape'] # Declaring a list
for fruit in fruits: # For each
    print(fruit)