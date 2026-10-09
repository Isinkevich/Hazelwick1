import random as r

num = r.randint(1,100)
ans = None
guess = 1

while True:
    ans = int(input("Enter a number 1-100: "))
    if ans > num:
        print("Your number is greater than the generated one")
        guess = guess + 1
    elif ans < num:
        print("Your number is smaller than the generated one")
        guess = guess + 1
    if num == ans or guess > 10:
        break

if ans == num:
    print(f"You won in {guess} tries.")
elif guess > 10:
    print("You lose")