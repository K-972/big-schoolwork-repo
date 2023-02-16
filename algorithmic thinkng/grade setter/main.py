import pandas as pd
import os
import datetime

# get the current working directory
cwd = os.getcwd()

# get the number of kids to input from user
number_of_inputs = int(input("Enter the number of kids to input: "))

# initialize a variable to keep track of how many kids have been entered
current_kids_done = 0

# get the maximum marks from user
max_marks = int(input("Enter the maximum marks: "))

# create an empty DataFrame to hold all the kids' data
df = pd.DataFrame(columns=['Name', 'Mark', 'Max Marks', 'Grade', 'Percentage'])

# define a function to get input from user, calculate grade and percentage, and write data to file
def main():
    # use the global keyword to modify the df variable, which is in the global scope
    global df

    # get input from user
    name = input("Enter the student's name: ")
    mark = int(input("Enter the student's mark: "))
    print()

    # calculate percentage
    percentage = (mark / max_marks) * 100
    percentage = round(percentage, 2)

    # calculate grade boundaries
    # 50%
    fail_grade_boundaries = (max_marks * 0.5)
    # 70%
    pass_grade_boundaries = (max_marks * 0.7)
    # 90%
    merit_grade_boundaries = (max_marks * 0.9)

    # determine the grade based on the mark
    if mark < fail_grade_boundaries:
        grade = "Fail"
    elif mark >= fail_grade_boundaries and mark < pass_grade_boundaries:
        grade = "Pass"
    elif mark >= pass_grade_boundaries and mark < merit_grade_boundaries:
        grade = "Merit"
    else:
        grade = "Distinction"

    # write the data to a file
    with open(f"grades_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", "a") as f:
        f.write(f"{name}, {mark}, {max_marks}, {grade}, {percentage}\n")

    # append the new data to the existing DataFrame
    new_data = pd.DataFrame({"Name": [name],
                             "Mark": [mark],
                             "Max Marks": [max_marks],
                             "Grade": [grade],
                             "Percentage": [percentage]})

    df = pd.concat([df, new_data], ignore_index=True)

    # write the updated DataFrame to an Excel file
    with pd.ExcelWriter(f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx") as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)

if __name__ == "__main__":
    # loop through the number of kids to input and call the main function for each kid
    for current_kid in range(number_of_inputs):
        main()
        current_kids_done += 1

    # write the complete DataFrame to the Excel file
    with pd.ExcelWriter(f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx") as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
