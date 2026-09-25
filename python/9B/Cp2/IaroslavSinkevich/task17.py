given = int(input("Give a time in minutes: "))

hr = given//60
minu = given%60

print(given,"minutes is", hr,"hour(s) and", minu, "minutes")