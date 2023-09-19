def addition(num1, num2):
        answer = num1 + num2
        print(answer)


def subtraction(num1, num2):
        answer = num1 - num2
        print(answer)
# form times no times


def times(num1, num2):
    answer = 0

    while num2 > 0:
        if num2 % 2 == 1:
            answer += num1

        num1 *= 2
        num2 //= 2
    print(answer)

def division(num1, num2):
    answer = num1 // num2
    print(answer)


# add menu

choice = input("add divide subtract multiply: ")

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))



#basics
if choice == "add":
    addition(num1, num2)

elif choice == "subtract":
    subtraction(num1, num2)

elif choice == "multiply":
    # form times no times
    times(num1, num2)


else:
    division(num1, num2)


