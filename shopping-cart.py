# Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total_price = price * quantity

print(f"Item name: {item}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total price: ${total_price}")