max_number = int(input("enter a max even number >> "))
sum = 0
def find_even(max_number, sum):
    for i in range(max_number):
        if i % 2 == 1:
            sum = sum + i
        else:
            pass
    print(sum)
find_even(max_number, sum)