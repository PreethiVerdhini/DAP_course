# program 1 : Create a dictionary with student names as keys and their marks as values.
#Allow the user to input a name and display the student's marks. If the student doesn't exist, show an appropriate message.

Students = {}
no_of_students = int(input("Enter total number of students: "))
for _ in range(no_of_students):
    Name = input("Enter the student name: ")
    Marks = int(input(f"Enter the marks for {Name}: "))
    Students[Name.lower()] = Marks  # Store names in lowercase for uniform search

print("\nStudent Records:")
for name, marks in Students.items():
    print(f"Student: {name}, Marks: {marks}")


search_student = input("Enter the name of the student to be searched: ").lower()

if search_student in Students:
    print(f"{search_student.capitalize()}'s marks: {Students[search_student]}")
else:
    print(f"No record found for student '{search_student.capitalize()}'")

