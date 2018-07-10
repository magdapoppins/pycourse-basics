# Function 1: definition (describe how to do something)
def hi(name):
    print("Hi, {}!".format(name))
    print("Are you on your way to the beach?")

# Function 1: call (do what you described)
# hi("Nina")

# Function 2: fibonacci nums printed
def fib_1(n):
    print("Fibonacci numbers in range 0, {}".format(n))
    a, b = 0, 1
    while a < n:
        print (a)
        a, b = b, a + b
    print()

fib_1(20)    

# Function 2: fibonacci nums as a return type
def fib_2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

my_numbers = fib_2(30)
print(my_numbers)