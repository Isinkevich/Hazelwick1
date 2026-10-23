dAge = 17
age = int(input("Enter your age:"))
time_left = dAge - age
if time_left <= 0:
    print("You are old enough to drive")
else:
    print(f"You can drive in {time_left} years")