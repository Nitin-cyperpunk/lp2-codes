def welcome():
    print("****** Welcome to Food Shop ******\n")

def info():
    name = input("Can I know your good name: ")
    print(f"\nHey {name}! Good to see you here!!!")
    print("You are in the right place, I will help you book your dish and drinks.\n")
    return name

def menu():
    print('''Here is your menu with their prices:
    1. Pizza - RS.200
    2. Mango Juice - RS.70
    3. Apple Juice - RS.80
    4. Burger - RS.100
    5. Cold Drink - RS.50
    6. Ice Cream - RS.120
    7. Sandwich - RS.90
''')

def order(price, product, name):
    print(f"\nThank you for choosing {product}!\n")
    print("Please give us some more information about you:")
    mob = input("Enter your mobile number: ")
    add = input("Enter your delivery address: ")

    print('''\nChoose mode of payment:
    1. Online
    2. Cash on delivery
    3. UPI
    4. Credit Card
    5. Debit Card''')
    
    pay = input("Enter your choice (1-5): ")
    payment_modes = {
        "1": "Online",
        "2": "Cash on delivery",
        "3": "UPI",
        "4": "Credit Card",
        "5": "Debit Card"
    }
    paymode = payment_modes.get(pay, "Online")  # default to Online if invalid

    print("\n******* Here is the detail of the selected order ******\n")
    print(f"Customer Name: {name}")
    print(f"Product Name: {product}")
    print(f"Price: RS.{price}")
    print(f"Mode of Payment: {paymode}")
    print(f"Delivery Address: {add}\n")

    b = input("Please confirm by pressing 1, else 0 to cancel: ")
    print()
    if b == "1":
        print("\n******* Your order is booked successfully *******")
        print(f"Customer Name: {name}")
        print(f"Product Name: {product}")
        print(f"Price: RS.{price}")
        print(f"Mode of Payment: {paymode}")
        print(f"Delivery Address: {add}\n")
        print("Thank you for your interest!!! Have a nice day!!!")
    else:
        print("***** Thank you for visiting!!! Have a nice day!!! *****")

def choice(name):
    products = {
        "pizza": 200,
        "mango juice": 70,
        "apple juice": 80,
        "burger": 100,
        "cold drink": 50,
        "ice cream": 120,
        "sandwich": 90
    }
    
    selected = input("Please type the name of the product you wish to order: ").lower()
    
    if selected in products:
        order(products[selected], selected.title(), name)
    else:
        print("\nYou have not selected any valid product... Thank you for visiting!!! Have a nice day!!!!")

# Run the food order program
welcome()
customer_name = info()
menu()
choice(customer_name)
