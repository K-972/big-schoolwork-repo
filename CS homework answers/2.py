def task_one():
    name = input("Input your name: ")
    if name.lower() == "hazel":
        print("Hello Hazel")
    else:
        print(f"We havent met yet, {name}")
    
    ############################
    ######### 4 marks ##########
    ############################

def task_two():
    temp = input("Enter the temperature")
    humidity = input("Enter the humidity")
    if window.lower() == “closed”:
        if temp > 25 or humidity < 50:
            print("Open the window")
        elif temp < 10 and humidity < 50:
            print("Close the window")

    ############################
    ######### 4 marks ##########
    ############################

def task_three():
    answer_one = "Error... enter a number from 0 to 14"
    answer_two = "ph is acidic"
    answer_three = "neutral"
    answer_four = "acidic"
    answer_five = "Error... enter a number from 0 to 14"

    ############################
    ######### 4 marks ##########
    ############################

def task_four():
    print(“Select one of the following options: ”)
    print(“Enter A for Multiply: ”)
    print(“Enter B for Divide: ”)
    print(“Enter C for Add: ”)
    print(“Enter D for Subtract: ”)
    print(“Enter E for Remainder Division: ”)
    choice = input("enter your choice: ")
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    match choice:
        case "A":
            answer = num1 * num1
            print(answer)
        case "B":
            answer = num1 / num1
            print(answer)
        case "C":
            answer = num1 + num1
            print(answer)
        case "D":
            answer = num1 - num1
            print(answer)
        case "E":
            answer = num1 % num1
            print(answer)
        case _:
            print("invalid response")

    ############################
    ######### 4 marks ##########
    ############################

def task_five():
    year = input("enter ayear: ")
    LeapYear = FALSE
    if (mod(Year, 4) == 0) then
        LeapYear = TRUE
    if (mod(Year,100) == 0) then 
        LeapYear = FALSE
    if (mod (Year,400) == 0) then
        LeapYear = TRUE
    if leapyear == True:
        print("leapyear")
    else:
        print("not a leap year")


    ############################
    ######### 4 marks ##########
    ############################



          
          
