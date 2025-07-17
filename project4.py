#conditional statement
print("1. This is the example of IF THE CONDITIONAL STATEMENT")
marks=87
if marks >= 90:
    print("you get a mobile phone")

print("Thank You")

print("2. This is the example of IF THE CONDITIONAL STATEMENT")
marks=97
if marks >= 90:
    print("you get a mobile phone")
print("Thank You")

print("3. This is the example of IF-ELSE CONDITIONAL STATEMENT")
marks=87
if marks >= 90:
    print("you get a mobile phone")
else:
    print("NO phone for 1 week")
print("Thank You")

print("4. This is the example of IF-ELIF-ELSE CONDITIONAL STATEMENT")
marks=87
if marks >= 90:
    print("you can goi to trip")
elif (marks >= 80) and (marks <90):
    print("you get a new phone")
elif (marks >= 70) and (marks <80):
    print("you will get a new book")
else:
    print("you will not get your back")

print("5. This is the example of NESTED IF STATEMENT CONDITIONAL STATEMENT")
marks=97
if marks >= 90:
    print("you will get new phone")
elif marks >=95:
    print("you can go to a trip")
else:
    print("no phone for a month")

print("6. This is the example of SHORT HAND IF CONDITIONAL STATEMENT")
marks=97
if marks >= 90:print("you will get a phone")

print("7. This is the example of SHORT HAND IF-ELSE CONDITIONAL STATEMENT")
marks=97
print("you will go to a trip")if marks>=90 else print ("you will not get phone for month")


