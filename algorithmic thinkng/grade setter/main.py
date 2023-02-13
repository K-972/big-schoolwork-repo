


def get_values():
    chlids_name = input("Enter the childs name: ")
    chlids_mark = input("Enter the childs mark: ")
    chlids_age = input("Enter the childs age: ")

    return chlids_name, chlids_mark, chlids_age


def main(chlids_name, chlids_mark, chlids_age):

    #############################
    ###     calculations      ###
    #############################

    if chlids_mark > 50:
        childs_grade = "fail"
    elif chlids_mark <= 50 and chlids_mark < 70:
        childs_grade = "pass"
    elif chlids_mark >= 70 and chlids_mark < 90:
        childs_grade = "merit"
    elif chlids_mark >= 90:
        childs_grade = "distinction"

    with open("grades.txt", "w") as f:
        f.write(chlids_name + "," + chlids_mark + "," + chlids_age + "," + childs_grade + "\n")


if __name__ == "__main__":
    get_values()
    main(*get_values())

    