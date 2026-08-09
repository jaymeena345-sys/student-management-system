import json
import os

FILE_NAME='student.json'
students=[]
#Loads students from file
def load_student():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as file:
            return json.load(file)
    return []

#Save students to file
def save_students(students):
    with open(FILE_NAME,'w') as file:
        json.dump(students,file,indent=4)


#Add a student
def add_student(students):
    name=input('Enter student name:')
    roll=input("Enter roll number; ")
    marks=float(input("Enter marks:"))

    student={
        'name':name,
        'roll':roll,
        'marks':marks
        }

    students.append(student)
    save_students(students)
    

#View all students 
def view_student(students):
    if len(students)==0:
        print('NO students records found.')
        return

    print('\n---Student Records---')

    for student in students:
        print(
            f'Name:{student['name']},'
            f'Roll No:{student['roll']},'
            f'Marks:{student['marks']}'
        )

#Search student
def search_student(students):
    roll=input('Enter roll number to be search:')

    for student in students:
        if student['roll']==roll:
            print('\nStudent Found:')
            print(f'Name:{student['name']}')
            print(f'Roll No:{student['roll']}')
            print(f'Marks:{student['marks']}')
        else:
            print('Student not found')

#Update student
def update_student(students):
    roll=input('Enter roll number to update:')

    for student in students:
        if student['roll']==roll:

            print('Leave input empty to keep old value')
            
            name=input('Enter new name:')
            marks=input('Enter new marks:')
            #roll=input('Enter new roll number:')

            if name:
                student['name']==name
            if marks:
                student['marks']==float(marks)

            save_students(students)

            print('Student updated successfully!')
            return
        print('Student not found')

#Delete student             
def delete_student(students):
    roll=input('Enter roll number to delete:')

    for student in students:
        if student['roll']==roll:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

        print("Student not found")


#Main menu
def main():
    while True:
        print('\n====Student Management System====')
        print('1.Add Student')
        print('2.View tudent')
        print('3.Search Student')
        print('4.Update  Student')
        print('5.Delete Student')
        print('6.Exit')

        choice=int(input('Enter your choice:'))

        if choice==1:
            add_student(students)
        elif choice==2:
            view_student(students)
        elif choice==3:
            search_student(students)
        elif choice==4:
            update_student(students)
        elif choice==5:
            delete_student(students)
        elif choice==6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!Try again")

#RUN PROGRAM
if __name__=="__main__":
    main()
