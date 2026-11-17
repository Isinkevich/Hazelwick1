shop = ["Milk", "Bread", "Baked Beans", "Bananas", "Butter", "Battleships"]
want = input("Enter your good for purchase: ").strip()

found = False
for item in shop:
    if want.lower() == item.lower():
        found = True
        break

if found:
    print("Your good is available for purchase!")
else:
    print("Your good is unavailable for purchase!")