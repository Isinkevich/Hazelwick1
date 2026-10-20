import random as r

score = 0

for i in range(20):
    guess = r.randint(1,4)
    num1 = r.randint(1,1000)
    num2 = r.randint(1,1000)
    match guess:
        case 1:
            actual = num1 + num2
            ans = int(input(f"{num1} + {num2} ="))
            if ans == actual:
                score = score + 1
        case 2:
            actual = num1 - num2
            ans = int(input(f"{num1} - {num2} ="))
            if ans == actual:
                score = score + 1
        case 3:
            actual = num1 * num2
            ans = int(input(f"{num1} * {num2} ="))
            if ans == actual:
                score = score + 1
        case 4:
            actual = num1 // num2
            ans = int(input(f"(Truncate to the nearest integer) {num1} / {num2} ="))
            if ans == actual:
                score = score + 1

print(score)