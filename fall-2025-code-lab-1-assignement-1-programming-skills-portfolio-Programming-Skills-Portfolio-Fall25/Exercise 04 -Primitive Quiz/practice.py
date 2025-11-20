# Ask the user a question about the capital of France
answer = input("What is the capital of France? ")

# Convert the answer to lowercase and remove extra spaces to ignore capitalization
if answer.strip().lower() == "paris":
    # If the answer is correct
    print("Correct!")
else:
    # If the answer is wrong
    print("Wrong! The correct answer is Paris.")
