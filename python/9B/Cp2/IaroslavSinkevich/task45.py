import random as r

num = r.randint(1,100)
ans = None
guess = 1

for guess in range(1,11):
    ans = int(input("Enter a number: "))
    if ans == num:
        print(f"You won in {guess} tries.")
        quit()
    elif num > ans:
        print("Your number is lower than it was generated.")
    elif num < ans:
            print("Your number is higher than it was generated.")

print("You lost.")