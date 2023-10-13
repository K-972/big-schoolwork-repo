def check_if_edit_parameters_correct(thing_to_check):
    pass_check = False
    while pass_check != True:
        prompt = input(f"Is {thing_to_check} correct or not y/n: ")
        if prompt.lower() == 'y':
            return thing_to_check
            pass_check = True
        elif prompt.lower() == 'n':
            thing_to_check = input("Enter the correct text: ")
        else:
            print("Invalid input. Please try again.")


thing_to_check = input("Enter the name: ")

check_if_edit_parameters_correct(thing_to_check)

print(thing_to_check)

key = "b'l3vZ2XL6fsl2UTCYeq-00k162exuUIrBC3_y96xFN5M='"
print(key)