num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num > 10:
    print(f"Invalid input. Please enter a number between 1 and 10.")
    num = int(input("Enter a number between 1 to 10: "))

print(f"You entered: {num}")