#program 2 : Take a student’s name and grade, and print a formatted report

name = input("Enter student name: ")
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = []
print("\nEnter marks out of 100:")
for subject in subjects:
    score = float(input(f"{subject}: "))
    marks.append(score)
total = sum(marks)
percentage = total / len(subjects)
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"
print("\n----- STUDENT REPORT -----")
print("Student:", name)
print("Total Marks:", total)
print("Final Grade:", grade)

