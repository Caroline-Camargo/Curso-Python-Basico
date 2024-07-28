
def get_name():
    return "Caroline"


# Files
'''
file = open('name', 'mode') # Open a file in write mode
file.write('text') # Write in the file
file.close() # Close the file
'''

name_file = 'file.txt' # File name


# Write in the file
write_file = open(name_file, 'w') # Open a file in write mode
write_file.write(f'Text to be written {get_name()}\n')
write_file.close()


# Read a file
read_file = open(name_file, 'r') # Open a file in read mode
reading = read_file.read() 
print(reading)
read_file.close()


# Other modes
#binary_file = open(name_file, 'wb') # Open a file in binary mode
#binary_file.close()

'''
r - read
w - write
a - append
b - binary
a - append
b - binary
r+ - read and write
w+ - write and read
a+ - append and read
rb - read binary
wb - write binary
ab - append binary
rb+ - read and write binary
wb+ - write and read binary
ab+ - append and read binary
'''
