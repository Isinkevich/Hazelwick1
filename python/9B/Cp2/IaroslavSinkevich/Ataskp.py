shop = ['milk','bread','baked beans','bananas','butter','battleships']
want = input("Enter your item: ")
for i in shop:
    if want.lower == i:
        print("Your item is on the list")
        print(f"Your item in number {shop + 1}")
        flag = True
    elif want.lower != i:
        print("Your item is not on the list")
        flag = False
    if flag == False or flag == True:
        break