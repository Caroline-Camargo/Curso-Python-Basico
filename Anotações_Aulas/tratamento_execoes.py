# Treating exceptions
'''
try:
    # code that may cause an exception
except Exception as e:
    # code that will be executed if an exception occurs
else:
    # code that will be executed if no exceptions occur
    
'''

def division(a, b):
    try:
        result =  a / b
        print(result)

    except ZeroDivisionError:
        print(f'Error: Impossible to divide by zero')
    except TypeError as e:
        print(f'Error: The data division type is incorrect. \nDetails: {e}')
    else:
        print('No exceptions occurred')
    
division(10, 0)
division(10, 'womakerscode')