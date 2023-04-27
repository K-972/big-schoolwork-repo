miles = int(input("enter number of miles: "))
age = int(input("enter age: "))

if miles >= 0 and miles <= 10000:
    if age >= 0 and age <= 5:
        print("true")
    else:
        pass
else:
    print("false")