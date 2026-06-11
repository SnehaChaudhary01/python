class Student:
    all_students = []
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    
    @classmethod
    def add_students(cls):
        stid = input("Enter your student id :")
        name = input("Enter your name :")
        age = int(input("Enter your age :"))
        course = input("Enter your course:")
        marks = int(input("Enter your marks: "))
        student = cls(stid, name, age, course, marks)
        cls.all_students.append(student)
        print(f"Student {name} added succesfully!\n")

        
def menu():
    while True:
        print("<<<<<<< STUDENTS MANAGEMENT SYSTEM >>>>>>>")
        print("1. Add Student")
        print("2. View Student")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice : ")
        if choice == "1":
            Student.add_students()
        elif choice == "2":
            Student.view_students()
        elif choice == "3":
            Student.delete_students()
        elif choice == "4":
            Student.update_students()
        elif choice == "5":
            print("Exiting Student Management System...")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    menu()
