import random as r
score = 0

for z in range(5):
    num = r.randint(0,100)
    guess = int(input("A random number is generated between 0 and 100. Guess it."))
    if guess == num:
        print("Bang on!")
        score = score + 10
    elif num-5 < guess < num+5:
        print("Close")
        score = score + 5
    elif num - 10 < guess < num + 10:
        print("Okay")
        score = score + 2
    else:
        print("Way off")
print("Your score is", score)