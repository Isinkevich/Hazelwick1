hei = int(input("Enter a height of triangle (in rows)"))
for i in range(hei):
    print("" + " " * ((i//2)- (i-1)) + "*" * (i+1))