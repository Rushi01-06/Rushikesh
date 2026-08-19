# 1. Create a dictionary containing student names and marks
student_marks = {
    "sid": 85,
    "harsh": 70,
    "parth": 92,
    "om": 58,
    "siva": 88
}
lowest_student = min(student_marks, key=student_marks.get)
print(f"Student Marks Dictionary: {student_marks}")
print(f"The student with the lowest marks is {lowest_student} with {student_marks[lowest_student]} marks.")
