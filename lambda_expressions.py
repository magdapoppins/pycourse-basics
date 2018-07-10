# Small anonymous functions can be created using the lambda keyword
def make_incrementor(i):
    return lambda x: x + i

my_incrementor = make_incrementor(3)
print(my_incrementor(2))