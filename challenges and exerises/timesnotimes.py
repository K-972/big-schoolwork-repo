print("This program multiplies two numbers without using the multiplication operator.")

try:
    num1 = int(input("Enter the first number: "))
except ValueError:
    print("Invalid input for the first number.")
    exit()

try:
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input for the second number.")
    exit()

def times(num1, num2):
    answer = 0

    while num2 > 0:
        if num2 % 2 == 1:
            answer += num1

        num1 *= 2
        num2 //= 2

    return answer

result = times(num1, num2)
print("The result is:", result)
