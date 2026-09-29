score = 0
q1 = float(input("What is 134 + 783? The answer is: "))

if q1 == 917:
    print("You are right")
    score = score + 1
elif q1 != 917:
    print("You are wrong")

q2 = float(input("What is 512 - 320? The answer is: "))

if q2 == 192:
    print("You are right")
    score = score + 1
elif q2 != 192:
    print("You are wrong")

q3 = float(input("What is 13 * 7? The answer is: "))

if q3 == 91:
    print("You are right")
    score = score + 1
elif q3 != 91:
    print("You are wrong")

q4 = float(input("What is 255 / 15? The answer is: "))

if q4 == 17:
    print("You are right")
    score = score + 1
elif q4 != 17:
    print("You are wrong")

print("You got", score, "out of 4")