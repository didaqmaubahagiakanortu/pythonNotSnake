# casting from str to int

str_numbers = '456'
str_numbers_to_int = int(str_numbers)
print('Before casting:', str_numbers, "the data type is", type(str_numbers))
print('After casting:', str_numbers_to_int, "the data type is", type(str_numbers_to_int))

# casting from int to str

integer = 12345
integer_to_str = str(integer)
print('Before casting:', integer, "the data type is", type(integer))
print('After casting:', integer_to_str, "the data type is", type(integer_to_str))

# casting from int to bool

num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))

num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))

# Coding comparison operators

8 == 8
8 != 9
8 > 9
8 < 9
8 <= 9
8 >= 9

# Coding logical operators

a = True
b = True
print(a and b)
print(a or b)
print(not b)

5 > 6 and 6 < 7

# coding arithmetic operators

e = 8
f = 2

sum = e + f
print(f'The sum of e with f is {sum}\n')

red = e - f
print(f'The red of e with f is {red}\n')

mul = e * f
print(f'The mul of e with f is {mul}\n')

div = e / f
print(f'The div of e with f is {div}\n')

mod = e % f
print(f'The mod of e with f is {mod}\n')

pow = e ** f
print(f'The pow of e with f is {pow}\n')

# coding input output

name = str(input('What is your name? '))
age = int(input("How old are you? "))

print('Name:', name)
print('Age:', age)

print('Hi all! I am', name, 'and I am', age, 'years old.')
print(f'Hi all! I am {name} and I am {age} years old.')
print(f'Hi all! I am %s and I am %d years old.'%(name, age))
print(30*'=')
print('Temperature Calculator Program')
print(30*'=')