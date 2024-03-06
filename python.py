class Student:
    def __init__(self, name, rollno, age):
        self.name = name
        self.rollno = rollno
        self.age = age

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, rollno, age):
        student = Student(name, rollno, age)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def display_students(self):
        if not self.students:
            print("No students added yet.")
        else:
            print("List of Students:")
            for i, student in enumerate(self.students, 1):
                print(f"{i}. Name: {student.name}, Roll No: {student.rollno}, Age: {student.age}")

    def edit_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                print(f"Editing student with roll number {rollno}:")
                student.name = input("Enter new name: ")
                student.age = input("Enter new age: ")
                print(f"Student with roll number {rollno} edited successfully.")
                return
        print(f"Student with roll number {rollno} not found.")

    def delete_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                self.students.remove(student)
                print(f"Student with roll number {rollno} deleted successfully.")
                return
        print(f"Student with roll number {rollno} not found.")

def main():
    student_manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            rollno = input("Enter student roll number: ")
            age = input("Enter student age: ")
            student_manager.add_student(name, rollno, age)
        elif choice == '2':
            student_manager.display_students()
        elif choice == '3':
            rollno = input("Enter roll number of student to edit: ")
            student_manager.edit_student(rollno)
        elif choice == '4':
            rollno = input("Enter roll number of student to delete: ")
            student_manager.delete_student(rollno)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
