
name = input("What is your name >> ")

times_table_var = int(input("what times table do you want to see? "))
start_num = int(input("what number do you want to start at? "))
end_num = int(input("what number do you want to end at? "))
print("\n")
print(f"Hi {name} ... here is your times table.")
print("-----------------------------------------------")


def times_table(times_table_var, start_num, end_num):
    answer = 0
    int(answer)
    while start_num != end_num:
        answer = int(times_table_var * start_num)
        print(f"{times_table} x {start_num} = {answer}")
        start_num += 1

    


times_table(times_table_var, start_num, end_num)