chlids_mark = int(input("enter chlids mark: "))

if chlids_mark < 50:
    childs_grade = "fail"
    
elif chlids_mark >= 50 and chlids_mark < 70:
    childs_grade = "pass"
elif chlids_mark >= 70 and chlids_mark < 90:
    childs_grade = "merit"
elif chlids_mark >= 90:
    childs_grade = "distinction"

print(childs_grade)