# Python Compound Interest Calculator

# I'm new to Python and I'm trying to create a compound interest calculator. I've created the code below but I'm having trouble with the compound interest formula. I'm not sure how to implement it into my code. Any help would be appreciated.

# Compound Interest Formula: A = P(1 + r/n)^(nt) where: A = the amount of money accumulated after n years, including interest. P = the principal amount (the initial amount of money) r = the annual interest rate (in decimal) n = the number of times that interest is compounded per year t = the time the money is invested for, in years.

# Here's my code so far:
principle = 0
rate = 0
time = 0
total = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero. Please try again.")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero. Please try again.")
    else:
        break

while True:
    time = int(input("Enter the time in year/s: "))
    if time < 0:
        print("Time can't be less than zero. Please try again.")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
