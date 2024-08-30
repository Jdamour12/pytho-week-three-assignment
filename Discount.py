''' Function to calculate the discount if discount is grater or equal to 20% and return the final price  or return the original price if not '''


def calculateDiscount(price, discount_percent):
    if discount_percent >= 20:
        price = price * discount_percent / 100
    else:
        price = price
    return price


# Prompting the use to insert price and discount percentage
price = input("Enter the price of the item: ")
price = int(price)
discount_percent = input("Enter the discount percentage: ")
discount_percent = int(discount_percent)

# Calling the calculateDiscount by assigning it to the variable called final_price
final_price = calculateDiscount(price, discount_percent)

# Printing the final price
print(f'Thank you for your order! Your final price will be: {final_price}')
