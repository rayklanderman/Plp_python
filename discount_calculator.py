# Title: Discount Calculator Program

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if applicable.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage
    :return: Final price after applying the discount, or the original price if discount is less than 20%
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the result
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
