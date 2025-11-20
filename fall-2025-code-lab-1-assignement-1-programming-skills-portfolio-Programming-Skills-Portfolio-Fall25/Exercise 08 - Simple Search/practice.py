# List of names
names = ["Lubna", "Misbaah", "Ateef", "Shagufta", "Shifana", "Lukman"]

# Ask the user for the name to search
search_name = input("Enter the name to search for: ").strip()

# Search the name in the list (case-insensitive)
found = False
for name in names:
    if name.lower() == search_name.lower():
        found = True
        break

# Print the result
if found:
    print(f"{search_name} found in the list! ✔️")
else:
    print(f"{search_name} not found in the list. ❌")

