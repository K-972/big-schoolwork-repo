import pandas as pd
import os
cwd = os.getcwd()


number_of_inputs = int(input("Enter the number of kids to input: "))
current_kids_done = 0
max_marks = int(input("Enter the maximum marks: "))

# create an empty DataFrame to hold all the kids' data
df = pd.DataFrame(columns=['Name', 'Age', 'Mark', 'max marks', 'grade', 'percentage'])

def main():
    global df  # use the global DataFrame

    chlids_name = str(input("Enter the childs name: "))
    chlids_mark = int(input("Enter the childs mark: "))
    print("\n")

    #############################
    ###     calculations      ###
    #############################

    percentage = (chlids_mark / max_marks) * 100
    percentage = round(percentage, 2)
    
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
        percentage = str(percentage)
        file.write(chlids_name + "," + chlids_mark + "," + childs_grade + "," + percentage + "\n")
    
    # append the new data to the DataFrame
    new_data = {'Name': chlids_name, 'Mark': chlids_mark, 'max marks': max_marks, 'grade': childs_grade, 'percentage': percentage}
    df = df.append(new_data, ignore_index=True)

if __name__ == "__main__":
    for current_kid in range(number_of_inputs):
        main()
        current_kids_done += 1

    # write the complete DataFrame to the Excel file
    with pd.ExcelWriter('output.xlsx') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
