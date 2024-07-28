# Lists
'''
myList = [] # Empty list
myList = [1, 2, 3, 4, 5] # List with elements
myList = myList.append() # Add an element to the list
myList = myList[0] # Accessing a list element
'''

fruits_list = [] # declaring an list
fruit = input('Type the fruit: ')
fruits_list.append(fruit) 
fruits_list.append('apple') 
fruits_list.append('banana')
fruits_list.append('grape')
print(fruits_list)


# Tuples
'''
myTuple = () # Empty tuple
myTuple = (1, 2, 3, 4, 5) # Tuple with elements
myTuple = myTuple[0] # Accessing a tuple element
!!! Tuples cannot have changed values 
'''

fruits_tuples = ('apple', 'banana', 'grape', 'strawberry')
print(fruits_tuples)
#fruits_tuples.append('orange') # Error



# Dictionaries
'''
myDictionary = {} # Empty dictionary
myDictionary = {'key1': 'value1', 'key2': 'value2'} # Dictionary with elements
myDictionary = myDictionary['key1'] # Accessing a dictionary element
myDictionary.keys() # Returns the keys of the dictionary
myDictionary.get('key1') # Returns the value of the key
myDictionary.pop('key1') # Removes the key and its value
'''

dictionary = {}
dictionary['apple'] = 'is a fruit'
dictionary['car'] = 'is a vehicle'
dictionary['cat'] = 'is an animal'
print(dictionary.values('apple'))