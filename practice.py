def process_cart(items,prices):
    total_price = 0
    for i in range(len(items)):
        if prices[i] < 0:
            print(f"Invalid price for {items[i]},skipping...")
            continue
        if items[i] == "Out of stock":
            print(f"{items[i]} is out of stock. Stopping the purchase process.")
            break  # Stop processing when an item is out of stock
        
        if items[i] == "Discount Coupon":
            pass  # Do nothing for discount coupons for now
        else:
            print(f"Adding {items[i]} to the cart, price: {prices[i]}")
            total_price += prices[i]  # Add item price to total
    
    return total_price  # Return the total price after processing the cart

# Simulating a shopping cart with two lists: one for items and one for prices
shopping_items = ["Laptop", "Mouse", "Discount Coupon", "Out of Stock", "Monitor", "Keyboard"]
shopping_prices = [800, 25, 0, 500, 150, -10]

# Call the function to process the shopping cart
total = process_cart(shopping_items, shopping_prices)
print(f"\nTotal price of items in the cart: ${total}")