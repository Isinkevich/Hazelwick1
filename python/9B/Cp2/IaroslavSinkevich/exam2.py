elec = input("Is your car electric? ")
hrs = None
while True:
    hrs = int(input("How many hours are you parking your vehicle?"))
    if hrs == 0:
        print("Your parking bill is £0")
        break
    elif elec == 'yes' or elec == 'It is':
        print("Your parking bill is £"+str(hrs * 2))
    else:
        print("Your parking bill is £"+str(hrs * 4))