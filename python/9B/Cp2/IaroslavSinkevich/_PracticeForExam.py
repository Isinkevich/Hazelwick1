import random as r

name = input("Enter your name: ")
numQ = int(input("Enter an amount of questions you would like (1-10):"))
MAX_QUES = 10
QAsked = 0
score = 0

if numQ > 10:
    print("This is not a valid amount of questions")

print("Welcome", name)

while QAsked <= MAX_QUES:
    QType = r.randint(1,5)
    num1 = r.randint(1,300)
    num2 = r.randint(1,300)
    match QType:
        case 1:
            RealAns = num1 + num2
            SAns = int(input(f"What is the for answer for: {num1} + {num2}:"))
            if RealAns == SAns:
                score = score + 10
        case 2:
            RealAns = num1 - num2
            SAns = int(input(f"What is the for answer for: {num1} - {num2}:"))
            if RealAns == SAns:
                score = score + 10
        case 3:
            RealAns = num1 * num2
            SAns = int(input(f"What is the for answer for: {num1} * {num2}:"))
            if RealAns == SAns:
                score = score + 10
        case 4:
            RealAns = num1 // num2
            SAns = int(input(f"What is the for answer for: {num1} // {num2} Truncate to integer, if needed:"))
            if RealAns == SAns:
                score = score + 10
        case 5:
            RealAns = num1 ** num2
            SAns = int(input(f"What is the for answer for: {num1} to the power of {num2}:"))
            if RealAns == SAns:
                score = score + 10
    QAsked += 1

percentage = score / (QAsked) * 100

if percentage >= 50:
    print("You passed")
    if percentage >= 80:
        print("Gold achievement")
    else:
        print("Silver achievement")
else:
    print("You Failed!")
    if percentage <= 20:
        print("You need extra practice")
    else:
        print("You are getting there")