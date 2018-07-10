# Define the range in which you hunt for primes
print("Searching for primes in given range:")
for i in range (1, 21):
    # Define the range of possible dividers
    for y in range(2, i):
        # If the number modulus the possible dividers equals zero, it is a product of these two
        if i % y == 0:
            print(i, "equals", y, "*", i//y)
            break
    else: 
        print(i, "is a prime")    

print("Searching for equal numbers in given range:")
for n in range(20, 29):
    if n % 2 == 0:
        print(n, "is even")
        # Go to next iteration!
        continue
    print(n, "is not even")    