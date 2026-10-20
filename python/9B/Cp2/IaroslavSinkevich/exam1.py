people = 0
while people < 8:
    height = int(input("Enter your height in cm:"))
    if height >= 120 and height < 140:
        adult = input("Are you riding with an adult?")
        if adult == 'yes' or adult == 'I am':
            print("Welcome aboard!")
            people = people + 1
        else:
            print("You are not allowed!")
    elif height >= 140:
        print("Welcome aboard!")
        people = people + 1
    else:
        print("You are not allowed!")
print("People limit reached! Please wait for next boarding!")