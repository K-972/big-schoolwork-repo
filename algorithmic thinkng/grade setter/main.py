import pandas as pd
import os
cwd = os.getcwd()

max_marks = 100

number_of_inputs = int(input("Enter the number of kids to input: "))
current_kids_done = 0
max_marks = int(input("Enter the maximum marks: "))

def main():

    chlids_name = str(input("Enter the childs name: "))
    chlids_mark = int(input("Enter the childs mark: "))
    chlids_age = input("Enter the childs age: ")
    print("\n")

    #############################
    ###     calculations      ###
    #############################

    percentage = (chlids_mark / max_marks) * 100

    if chlids_mark < 50:
        childs_grade = "fail"
        
    elif chlids_mark >= 50 and chlids_mark < 70:
        childs_grade = "pass"
    elif chlids_mark >= 70 and chlids_mark < 90:
        childs_grade = "merit"
    elif chlids_mark >= 90:
        childs_grade = "distinction"

    with open("grades.txt", "a") as file:
        chlids_mark = str(chlids_mark)
        file.write(chlids_name + "," + chlids_mark + "," + chlids_age + "," + childs_grade + percentage + "\n")
    

    # create a sample DataFrame
    data = {'Name': [chlids_name],
            'Age': [chlids_age],
            'Mark': [chlids_mark],
            'max marks': [max_marks],
            'grade': [childs_grade],
            'percentage': [percentage]}
    df = pd.DataFrame(data)

    # write the DataFrame to an Excel file
    with pd.ExcelWriter('output.xlsx') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)



if __name__ == "__main__":
    for current_kid in range(number_of_inputs):
        main()
        current_kids_done += 1

    