students_names = input("Enter your name:")
students_marks = int(input("Enter your marks:"))

# the conditons of the marks and gardes.
if students_marks >= 80:
    students_marks = 'A'
    print(f"{students_names} you  got the {students_marks} ")
elif students_marks >= 60:
    students_marks = 'B'
    print(f"{students_names} you got the {students_marks}")  
elif students_marks >= 40:
    students_marks = 'C'
    print(f"{students_names} you got the {students_marks}")
elif students_marks >= 30:
    students_marks = 'F'
    print(f"{students_names} you got the {students_marks}")
else:
    print("Your are fail in the examination.")