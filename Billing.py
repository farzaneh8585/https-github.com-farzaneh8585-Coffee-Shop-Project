from Order import orders

def calculate_total():
    total = 0
    for order in orders:
        total += order['price'] * order['quantity']
    return total

def calculate_discount(total_amount):
    if total_amount > 1000000:
        discount = total_amount * 0.10
    else:
        discount = 0
    return discount

def print_invoice():
    if len(orders) == 0:
        print("\nThere are no orders to print an invoice for.")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final_price = total - discount

    print("\n========== INVOICE ==========")
    for order in orders:
        print(f"{order['name'].capitalize()} x {order['quantity']}")
    
    print("-" * 29)
    print(f"Total Amount:    {total:,} Tomans")
    print(f"Discount (10%):  {discount:,} Tomans")
    print(f"Final Price:     {final_price:,} Tomans")
    print("=============================")
