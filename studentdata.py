
name = input("Enter name of student: ")
roll_no = int(input("Enter Roll no: "))
marks = int(input("Enter the marks: "))


if marks >= 90:
    print("Grade -> 10    OUTSTANDING")
elif marks >= 80 and marks < 90:
    print("Grade -> 9     VERY GOOD")
elif marks >= 70 and marks < 80:
    print("Grade -> 8     GOOD")
elif marks >= 60 and marks < 70:
    print("Grade -> 7     AVERAGE")
elif marks >= 50 and marks < 60:
    print("Grade -> 6     PASS")
else:
    print("Grade -> 0     FAIL")
