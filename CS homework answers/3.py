def task_1():
    count = 0
    list = []
    while count != 5:
        letter = input('enter a letter: ')
        list.append(letter.lower())
        count = count + 1
    lowest = list[0]
    highest = list[0]
    for letter in list:
        if letter > highest:
            highest = letter
        elif letter < lowest:
            lowest = letter
    print(f"highest = {highest}, lowest = {lowest} ")

    ############################
    ######### 6 marks ##########
    ############################

def task_two():
    password = “Tues1212”
    attempt_num = 0
    password_attempt = input("enter password attempt: ")
    while attempt_num != 3:
        password_attempt = input("enter password attempt: ")
        if password_attempt != password:
            print('incorrect guess')
            attempt_num = attempt_num + 1
        else:
            print("correct password")

    ############################
    ######### 6 marks ##########
    ############################

def task_three():
    traceTable1 = """0	0	100	0	
2	2	100	2	
7	7	100	9	
3	7	3	12	
8	8	3	20	
-1	8	3	20	Max sunshine hours: 8
Min sunshine hours: 3
Total sunshine hours: 20"""

    ############################
    ######### 3 marks ##########
    ############################

problem1 =  "The problem with the original algorithm is that it does not correctly initialize the maxHours, minHours, and totalSunshine variables. They are initially set to values that may not be accurate for the given input data, and it assumes that the user will input at least one positive value before entering -1. If the user doesn't input any positive values, the results will be incorrect."

    ############################
    ######### 2 marks ##########
    ############################

traceTable2 = """0	0	100	0	
2	2	100	2	
7	7	100	9	
3	7	3	12	
8	8	3	20	
-1	8	3	20	Max sunshine hours: 8
Min sunshine hours: 3
Total sunshine hours: 20"""

    ############################
    ######### 2 marks ##########
    ############################


############## total = 19