# Make a string question and an array of possible answers
question = "Do you prefer coffee or tea?"
possible_answers = ["Coffee", "Tea"]
user_answer = None

while user_answer not in possible_answers:
    # Print the question and each one of the possible answers
    print(question)
    for answer in possible_answers:
        print(answer)

    user_answer = input(">>> ")    