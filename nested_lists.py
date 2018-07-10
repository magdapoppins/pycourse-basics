# Create a list with nested lists
nested_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Print the list
print(nested_list)

# Print each individual element of the list
for row in nested_list:
    for element in row:
        print(element)

# Print a 2D-plane with "X" representing each element of the list
for row in nested_list:
    print("-------------")
    built_row = "|"
    for element in row:
        built_row += " X |"

    print(built_row)

print("-------------")

