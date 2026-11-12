from Menu import menu

orders = []

def add_order():
    item_name = input("Enter product name: ").lower()
    
    if item_name in menu:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return
                
            order = {
                "name": item_name,
                "price": menu[item_name],
                "quantity": quantity
            }
            orders.append(order)
            print(f"{quantity} {item_name}(s) added to your order.")
            
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Sorry, this item is not on the menu.")

def show_orders():
    if len(orders) == 0:
        print("\nYour order list is empty.")
        return

    print("\n--- Your Orders ---")
    for order in orders:
        print(f"{order['name'].capitalize()} | Price: {order['price']:,} | Quantity: {order['quantity']}")
