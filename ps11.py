# Create a dictionary with student names and marks
student_marks = {
    "sid": 85,
    "shailu": 92,
    "goku": 78,
    "harsh": 95,
    "sid": 88
}
top_student = max(student_marks, key=student_marks.get)
highest_mark = student_marks[top_student]
print(f"Highest scorer: {top_student} with {highest_mark} marks")
