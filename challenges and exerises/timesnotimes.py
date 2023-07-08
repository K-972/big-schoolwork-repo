print("This programme will times two numbers without using the times function")
try:
    num1 = int(input("First number:"))
except ValueError:
    print("invalid input")
    exit()
try:
    num2 = int(input("Second number:"))
except ValueError:
    print("invalid input")
    exit()

def times(num1, num2):
    count = 1
    answer = 0

    while count <= num2:

        
        answer = answer + num1
        count += 1
    
    return answer

result = times(num1, num2)
print(result)
