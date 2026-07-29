# menu of restaurant
menu = {
    "Breakfast": {
        "Pancakes": 10.99,
        "Omelette": 8.99,
        "Toast": 4.99
        
    },
    "Lunch": {
        "Caesar Salad": 12.99,
        "Grilled Chicken Sandwich": 15.99,
        "Fish and Chips": 18.99
    },
    "Dinner": {
        "Steak": 25.99,
        "Salmon": 22.99,
        "Pasta": 16.99
    }
}
print("Welcome to our restaurant! Here is our menu:")
for category, items in menu.items():  # category: receives each top-level key (meal category); items: receives the associated sub-dictionary of dishes; in: iteration keyword; menu.items(): returns iterable of (key, value) pairs
    print(f"\n{category}:")
    for name, price in items.items():  # name: receives each dish name; price: receives the dish price; in: iteration keyword; items.items(): returns iterable of (name, price) pairs
        print(f"  {name} - ${price:.2f}")

# Build a flat lookup from dish name to price for easy ordering
order_total = 0.0
dish_lookup = {}
for cat, items in menu.items():  # cat: category name; items: dishes dict
    for dish_name, dish_price in items.items():
        dish_lookup[dish_name] = dish_price

# Repeatedly prompt the user for dishes until they type 'done'
while True:
    choice = input("Please enter the name of the dish you would like to order (or type 'done' to finish): ")
    if choice.strip().lower() == 'done':
        break
    if choice in dish_lookup:
        order_total += dish_lookup[choice]
        print(f"{choice} has been added to your order.")
    else:
        print(f"Sorry, {choice} is not on the menu.")

print(f"\nYour total order amount is: ${order_total:.2f}")