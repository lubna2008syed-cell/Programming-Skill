# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
    num = int(input("Enter a number: "))  # Ask the user for a number
    result = check_even_odd(num)          # Pass it to the function
    print(result)                          # Print the returned message

# Ensure main runs when the script is executed directly
if __name__ == "__main__":
    main()
