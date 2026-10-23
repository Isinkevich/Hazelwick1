A = 0
B = 0
C = 0
vote = ""

while vote.lower() != 'end':
    vote = input("Choose to vote for A B C \nWrite 'END' to finish voting:")
    if vote.capitalize() == "A":
        A = A + 1
    elif vote.capitalize() == "B":
        B = B + 1
    elif vote.capitalize() == "C":
        C = C + 1

print(f"There are {A + B + C} votes")
print(f"A got {A} votes.")
print(f"B got {B} votes.")
print(f"C got {C} votes.")