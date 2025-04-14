# program 1 : Manage Student Data Using Tuples and Various Methods
students = [
    ("Pree",1, (85, 90, 80), "A"),
    ("Jay",2, (75, 78, 72), "B"),
    ("Shalu",3, (92, 88, 95), "A"),
]


def display_students(student_list):
    print("\nStudent Records:")
    for student in student_list:
        print(f"Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}, Grade: {student[3]}")


def add_student():
    name = input("Enter Student Name: ")
    roll_no = int(input("Enter Roll Number: "))
    marks = tuple(map(int, input("Enter 3 Marks (comma separated): ").split(",")))
    grade = input("Enter Grade: ")
    students.append((name, roll_no, marks, grade))
    print(f"\nStudent {name} added successfully!")


def search_student():
    roll_no = int(input("Enter Roll Number to Search: "))
    for student in students:
        if student[1] == roll_no:
            print(f"\nStudent Found: Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}, Grade: {student[3]}")
            return
    print("\nStudent not found.")


def calculate_total_marks():
    print("\nTotal Marks for Each Student:")
    for student in students:
        total_marks = sum(student[2])
        print(f"Name: {student[0]}, Roll No: {student[1]}, Total Marks: {total_marks}")


def update_grade():
    roll_no = int(input("Enter Roll Number to Update Grade: "))
    new_grade = input("Enter New Grade: ")
    global students
    students = [(s[0], s[1], s[2], new_grade) if s[1] == roll_no else s for s in students]
    print(f"\nGrade updated for Roll No {roll_no}.")


def remove_student():
    roll_no = int(input("Enter Roll Number to Remove: "))
    global students
    students = [s for s in students if s[1] != roll_no]
    print(f"\nStudent with Roll No {roll_no} removed successfully!")

# Interactive menu for user input
while True:
    print("\nMenu:")
    print("1. Display All Students")
    print("2. Add a New Student")
    print("3. Search for a Student")
    print("4. Calculate Total Marks")
    print("5. Update a Student's Grade")
    print("6. Remove a Student")
    print("7. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        display_students(students)
    elif choice == "2":
        add_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        calculate_total_marks()
    elif choice == "5":
        update_grade()
    elif choice == "6":
        remove_student()
    elif choice == "7":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
