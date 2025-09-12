def calculate_discount(price, discount):
    """Calculates final price after applying discount percentage"""

    # Make sure valid discount
    if discount < 0 or discount > 100:
        raise ValueError("Discount percentage must be between 0 and 100")

    # Subtract discount amount from price
    final_price = price - (price * (discount / 100))
    return final_price

if __name__ == "__main__":
    price = float(input("Enter price: "))
    discount = float(input("Enter discount percentage: "))
    print(f"Final price: {calculate_discount(price, discount)}")