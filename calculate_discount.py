def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price
def main():
    price = float(input("Enter the price: "))
    discount_percent=float(input("Enter the discount percent: "))
    final_price=calculate_discount(price, discount_percent)
    final_price = round(final_price, 2)
    if final_price == price:
        print("Original price", final_price)
    else:
        print("Final Price: ", final_price)
if __name__ == "__main__":
    main()