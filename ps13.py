# Create a dictionary of students and marks
student_marks = {
    "Aarav": 85,
    "Diya": 92,
    "Kabir": 78,
    "Ananya": 90,
    "Rohan": 88
}
total_marks = sum(student_marks.values())
total_students = len(student_marks)
average_marks = total_marks / total_students

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
