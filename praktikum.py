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

# coding conditionals and exception handling

try:
    your_GPA = float(input("Enter your GPA: "))
    if 4.0 >= your_GPA >= 0.0:
        if 4.0 >= your_GPA >= 3.80:
            print(f"You've got a magna cumlaude with your {your_GPA} GPA.")
        elif 3.50 <= your_GPA < 3.80:
            print(f"Cool!! You've got a cumlaude with your {your_GPA} GPA")
        elif 3.00 <= your_GPA < 3.50:
            print(f"You've got a stable GPA tho")
        elif your_GPA < 3.0:
            print(f"You need a stable GPA")
        else:
            print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
except:
    print("Please enter a valid GPA")

try:
    status_code = int(input("Enter your status code: "))
    print("Your code means...")
    match status_code:
        case 200:
            print("Success!")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 402:
            print("Payment Required")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
except:
    print("Please enter a valid status code")

a = 3
b = "Even Numbers" if a % 2 == 0 else "Odd Numbers"
print(b)

for i in range(5):
    print(i)
0
1
2
3
4

for i in range(5):
    print("Data science is easy!")

print(50*"=")

for i in range(1, 5, 2):
    print("Data science is easy!")

word = "I want to master data science"
for letter in word:
    print(letter)

for m, n in enumerate(word):
    print(f"Index {m}. {n}")

for i in range(5,1,-1):
    print("I want big data's")

for i in range(5):
    if i == 2:
        continue 
    if i == 4:
        break 
    print(i)

count = 0
while count < 4:
    print("Keep the spirits up interns!")
    count += 1