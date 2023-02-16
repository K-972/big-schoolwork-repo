import pandas as pd
import os
cwd = os.getcwd()

number_of_inputs = int(input("Enter the number of kids to input: "))
current_kids_done = 0
max_marks = int(input("Enter the maximum marks: "))

# create an empty DataFrame to hold all the kids' data
df = pd.DataFrame(columns=['Name', 'Mark', 'Max Marks', 'Grade', 'Percentage'])

def main():
    global df
    # get input from user
    name = input("Enter the student's name: ")
    mark = int(input("Enter the student's mark: "))
    print()

    # calculate grade and percentage
    percentage = (mark / max_marks) * 100
    percentage = round(percentage, 2)

    # calculate grade boundries

    # 50%
    fail_grade_boundries = (max_marks * 0.5)
    # 70%
    pass_grade_boundries = (max_marks * 0.7)
    # 90%
    merit_grade_boundries = (max_marks * 0.9)

    if mark < fail_grade_boundries:
        grade = "Fail"
    elif mark > fail_grade_boundries and mark < pass_grade_boundries:
        grade = "Pass"
    elif mark > pass_grade_boundries and mark < merit_grade_boundries:
        grade = "Merit"
    elif mark > merit_grade_boundries:
        grade = "Distinction"

    with open("grades.txt", "a") as f:
        f.write(f"{name}, {mark}, {max_marks}, {grade}, {percentage}\n")

    # append the new data to the existing DataFrame
    new_data = pd.DataFrame({"Name": [name],
                             "Mark": [mark],
                             "Max Marks": [max_marks],
                             "Grade": [grade],
                             "Percentage": [percentage]})

    df = pd.concat([df, new_data], ignore_index=True)

    # write the updated DataFrame to an Excel file
    with pd.ExcelWriter("output.xlsx") as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)

if __name__ == "__main__":
    for current_kid in range(number_of_inputs):
        main()
        current_kids_done += 1

    # write the complete DataFrame to the Excel file
    with pd.ExcelWriter('output.xlsx') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
