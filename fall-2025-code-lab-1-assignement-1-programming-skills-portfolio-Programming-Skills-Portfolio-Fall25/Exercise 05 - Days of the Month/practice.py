# Dictionary mapping month numbers to number of days
month_days = {
    1: 31,
    2: 28,  # February default
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user to input a month number
month = int(input("Enter the month number (1-12): "))

# Check if input is valid
if 1 <= month <= 12:
    print(f"Month {month} has {month_days[month]} days.")
else:
    print("Invalid month number! Please enter a number from 1 to 12.")
