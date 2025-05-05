def show_menu():

  print("\n🍔 Welcome to QuickBite Food Chatbot 🍟")
  print("Here is our menu:")
  print("1. Burger - ₹100")
  print("2. Pizza - ₹200")
  print("3. Fries - ₹80")
  print("4. Coke - ₹40")

def take_order():
  menu = {
    "burger": 100,
    "pizza": 200,
    "fries": 80,
    "coke": 40
  }
  order = {}
  while True:
    item = input("\nWhat would you like to order? (type 'done' to finish):").lower()
    if item == 'done':
      break
    elif item in menu:
      qty = int(input(f"How many {item}s? "))
      order[item] = order.get(item, 0) + qty
    else:
      print("Sorry, we don't have that item.")
  return order, menu

def show_bill(order, menu):
  print("\n  Your Bill:")
  total = 0
  for item, qty in order.items():
    price = menu[item] * qty
    print(f"{item.title()} x {qty} = ₹{price}")
    total += price
  print(f"Total Amount: ₹{total}")
  print("Thank you for ordering !")


# ---- Main Program ----
show_menu()
order, menu = take_order()
if order:
 show_bill(order, menu)
else:
 print("No order placed.") 