# Define the correct password
correct_password = "12345"

# Ask the user until they will enter the correct password
password = input("Enter the password: ")

# Loop until the password turns out to be correct
while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter the password: ")

# When correct password is being entered
print("Access granted! ✔️")