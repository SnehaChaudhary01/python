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

     @classmethod
    def view_students(cls):
        if len(cls.all_students) == 0:
            print("No Students Found!")
            return
        print("\n==== STUDENT LIST ====")
        for student in cls.all_students:
            student.show_details()

    @classmethod
    def delete_students(cls):
        stid = input("Enter Student ID to delete: ")
        student = cls.find_student_by_stid(stid)
        if student:
            cls.all_students.remove(student)
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    @classmethod
    def update_students(cls):
        stid = input("Enter Student ID: ")
        student = cls.find_student_by_stid(stid)
        if student:
            print("\nLeave blank if you don't want to change a field.")
            new_name = input("New Name: ")
            new_age = input("New Age: ")
            new_course = input("New Course: ")
            new_marks = input("New Marks: ")
            if new_name:
                student.name = new_name
            if new_age:
                student.age = int(new_age)
            if new_course:
                student.course = new_course
            if new_marks:
                student.marks = int(new_marks)
            print("Student updated successfully!")
        else:
            print("Student not found!")

    @classmethod
    def find_student_by_stid(cls, stid):
        for student in cls.all_students:
            if student.student_id == stid:
                return student
        return None
    


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
