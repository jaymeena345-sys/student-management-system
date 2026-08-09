import json
import os

FILE_NAME = "students.json"

# Load students from JSON file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save students to JSON file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# 1. Add a new student
def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    
    # Check if roll number already exists
    for student in students:
        if student["roll"] == roll:
            print("Student with this roll number already exists!")
            return

    # Basic error handling for marks
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid input! Marks should be a number.")
        return

    new_student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(new_student)
    save_students(students)
    print("Student added successfully!")

# 2. View all students
def view_students(students):
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"Name: {student['name']}, Roll No: {student['roll']}, Marks: {student['marks']}")

# 3. Search for a student
def search_student(students):
    roll = input("Enter roll number to search: ")
    found = False

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll']}")
            print(f"Marks: {student['marks']}")
            found = True
            break

    if not found:
        print("Student not found.")

# 4. Update student details
def update_student(students):
    roll = input("Enter roll number to update: ")
    found = False

    for student in students:
        if student["roll"] == roll:
            found = True
            print("Leave input empty to keep old value.")
            
            new_name = input("Enter new name: ")
            new_marks = input("Enter new marks: ")

            if new_name != "":
                student["name"] = new_name

            if new_marks != "":
                try:
                    student["marks"] = float(new_marks)
                except ValueError:
                    print("Invalid marks entered! Marks not updated.")

            save_students(students)
            print("Student updated successfully!")
            break

    if not found:
        print("Student not found.")

# 5. Delete a student
def delete_student(students):
    roll = input("Enter roll number to delete: ")
    found = False

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            found = True
            break

    if not found:
        print("Student not found.")

# Main function to run the program
def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__== "__main__":
    main()
