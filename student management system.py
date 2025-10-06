# Student Management System using Class and Object

class Student:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # 1. Accept student details
    def accept(self, roll_no, name, age, marks):
        student = Student(roll_no, name, age, marks)
        self.students.append(student)
        print("Student record added successfully.\n")

    # 2. Display all students
    def display(self):
        if not self.students:
            print("No student records found.\n")
        else:
            print("\n--- Student Records ---")
            for student in self.students:
                student.display()
            print("------------------------\n")

    # 3. Search student by Roll No
    def search(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent Found:")
                student.display()
                return student
        print("Student not found.\n")
        return None

    # 4. Delete student record
    def delete(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student record deleted successfully.\n")
                return
        print("Student not found.\n")

    # 5. Update student record
    def update(self, roll_no, name=None, age=None, marks=None):
        student = self.search(roll_no)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if marks:
                student.marks = marks
            print("Student record updated successfully.\n")


# Main program
def main():
    system = StudentManagementSystem()

    while True:
        print("===== Student Management System =====")
        print("1. Accept Student Details")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            marks = input("Enter Marks: ")
            system.accept(roll_no, name, age, marks)

        elif choice == '2':
            system.display()

        elif choice == '3':
            roll_no = input("Enter Roll No to Search: ")
            system.search(roll_no)

        elif choice == '4':
            roll_no = input("Enter Roll No to Delete: ")
            system.delete(roll_no)

        elif choice == '5':
            roll_no = input("Enter Roll No to Update: ")
            name = input("Enter New Name (leave blank to skip): ")
            age = input("Enter New Age (leave blank to skip): ")
            marks = input("Enter New Marks (leave blank to skip): ")
            system.update(roll_no, name or None, age or None, marks or None)

        elif choice == '6':
            print("Exiting... Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
