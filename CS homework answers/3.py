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
