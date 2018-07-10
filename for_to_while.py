# Display the options iterating over the list with a for-loop
breakfast_options = ["oatmeal", "a toast", "an omelet"]
print("--- Breakfast ---")
for option in breakfast_options:
    print("Would you like {}?".format(option))

# Display the options using the indeces of the list items
snack_options = ["cookies", "an apple", "juice"]
index = 0
print("--- Snack ---")
while index < len(snack_options):
    print("Would you like {}?".format(snack_options[index]))
    index += 1