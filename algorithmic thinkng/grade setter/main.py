# import required libraries
import warnings

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import os

# get current working directory
cwd = os.getcwd()

# get user input for number of kids and maximum marks
number_of_inputs = int(input("Enter the number of kids to input: "))
max_marks = int(input("Enter the maximum marks: "))

# create an empty DataFrame to hold all the kids' data
df = pd.DataFrame(columns=['Name', 'Mark', 'Max Marks', 'Grade', 'Percentage'])

# define main function to get user input, calculate grades, and append data to DataFrame
def main():

    # access the global DataFrame variable
    global df

    # get input from user
    name = input("Enter the student's name: ")
    mark = int(input("Enter the student's mark: "))
    print()

    # calculate grade and percentage
    percentage = (mark / max_marks) * 100
    percentage = round(percentage, 2)

    # calculate grade boundaries via percentage
    fail_grade_boundaries = (max_marks * 0.5)  # 50%
    fail_grade_boundaries = round(fail_grade_boundaries)
    pass_grade_boundaries = (max_marks * 0.7)  # 70%
    pass_grade_boundaries = round(pass_grade_boundaries)
    merit_grade_boundaries = (max_marks * 0.9)  # 90%
    merit_grade_boundaries = round(merit_grade_boundaries)

    # determine the grade based on the mark
    if mark < fail_grade_boundaries:
        grade = "Fail"
    elif mark >= fail_grade_boundaries and mark < pass_grade_boundaries:
        grade = "Pass"
    elif mark >= pass_grade_boundaries and mark < merit_grade_boundaries:
        grade = "Merit"
    elif mark >= merit_grade_boundaries:
        grade = "Distinction"

    # append the new data to the existing DataFrame
    new_data = pd.DataFrame({"Name": [name],
                             "Mark": [mark],
                             "Max Marks": [max_marks],
                             "Grade": [grade],
                             "Percentage": [percentage]})

    df = pd.concat([df, new_data], ignore_index=True)

    # writes the data to a text file for backup and checking correct input is being logged
    with open("grades.txt", "a") as txt_file:
        txt_file.write(f"{name}, {mark}, {max_marks}, {grade}, {percentage}\n")

# checks if this is the main prograam and run the main function for the number of kids specified
if __name__ == "__main__":
    for current_kid in range(number_of_inputs):
        main()

    #write the complete DataFrame to an Excel file named output
    with pd.ExcelWriter('output.xlsx') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
