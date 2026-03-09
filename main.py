""" EX No.1.1 """
""" printing data types """

score = 85
average = 85.5
passed = True

""" VARIABLES """

print(score)
print(average)
print(passed)

""" DATA TYPES """

print(type(score))
print(type(average))
print(type(passed))

""" EX No.1.2 """
""" Arithmetic and Expressions """
""" Question No.1 """

x = (10 + 3) * 2 - 4

print(x)

""" Question No.2 """

intdiv = 17 // 5 

print(intdiv)

remainder = 17 % 5 

print(remainder)

""" Question No.3 """

a = 2**5

print(a)

""" EX No.1.3 """
""" Comparison and Logical Operators """
""" Question No.1 """

a = 10 
b = 20

print(a<b)
print(a == 10 and b == 20)
print(not (a > b))


""" EX No.1.4 """
""" Complex Expressions """
""" Question No.1 """

c = (5 + 3) * 2 - 4 ** 2 // 3

print(c)

""" Question No.2 """

d = 10 % 3 + 2 ** 3 - 1

print(d)

""" Question No.3 """

x = 5
y = 3
z = 2

xyz = (x + y) * z - x // y

print(xyz)

""" EX No.1.5 """
""" Operator Precedence"""
""" Question No.1 """

e = 2 + 3 * 4 - 1

print(e)

"""Without parentheses → Python follows operator precedence,
where multiplication happens before addition and subtraction."""


""" Question No.2 """

f = (2 + 3) * (4 - 1)

print(f)

"""With parentheses → The expressions inside parentheses are calculated first,
which changes the order of operations and therefore the final result."""

""" EX No.1.6 """
""" Type Conversion Practice """
""" Question No.1 """

print(int(True))

h = int(False)

print(h)

i = float(100)

print(i)

j = int(3.14)

print(j)

""" Part 3: Input and Type Casting """
""" EX No.3.1 """
""" Basic Input """
""" Question No.1 """

number = input("Enter a number: ")

number_int = int(number)

print("You Entered:", number_int)

""" Question No.2 """

number_1 = input("Enter a first number: ")
number_2 = input("Enter a second number: ")

sum = (int(number_1) + float(number_2))
product = (int(number_1) * float(number_2))

print("Your Sum", sum)
print("Your Product", product)