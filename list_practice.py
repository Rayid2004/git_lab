'''PART A '''
''' 1. LIST COPMREHENSION LIST '''
list = [x for x in range(1,10)]
print(list)

''' 2. SQUARES OF 1-8 '''
squares = [x**2 for x in range(1,8)]
print(squares)


''' 3.LIST COMPREHENSION EVEN '''
evens = [x for x in range(20) if x % 2 == 0]
print(evens)


words = ['python', 'java', 'ai', 'data']
upper = [w.upper() for w in words]
print(upper)

# Create expression 



''' 6. cubes OF 1-5 '''
cubes = [x**3 for x in range(1,5)]
print(cubes)

list_2 = [x for x in range(10,15)]
print(list_2)

''' 8. filter '''
marks = [45,78,90,34,67,88,50]
highest_marks = [x for x in marks if x > 60]
print(highest_marks)

'''PART.B '''
''' 9. REMOVING NEGATIVE NUMBERS'''
numbers = [-5,3,-1,9,-7,6]
positive_numbers = [x for x in numbers if x >= 0 ]
print(positive_numbers)

# sir example 
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x)
    inner()
    print(x)
outer()
print(x)

# no.1
x = 'global'
def outer():
    
    def inner():
        x = 'local'
        print(x)
    inner()
    print(x)
outer()
print(x)

# no.2 
x = 'global'
def outer():
    # x = enclosing
    def inner():
        x = 'local'
        print(x)
    inner()
    print(x)
outer()
print(x)

# no.3
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        # x = 'local' 
        print(x)
    inner()
    print(x)
outer()
print(x)
        
        
