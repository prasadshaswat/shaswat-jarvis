#a program that simulates a school management system with classes for school, student, and teacher. The student and teacher classes should have methods to display their details. The school class should have methods to add students and teachers to the school. The school should have a method to display the details of all students and teachers in the school.
import random
class student:
    def __init__(self,name,rollno,standard):
        self.name=name
        self.rollno=rollno
        self.standard=standard
    def display(self):
        print("Name:",self.name)
        print("Roll number:",self.rollno)
        print("Standard:",self.standard)
class teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def display(self):
        print("Name:",self.name)
        print("Subject:",self.subject)
class school:
    def __init__(self):
        self.students={}
        self.teachers={}
    def add_student(self,name,rollno,standard):
        s=student(name,rollno,standard)
        self.students[rollno]=s
        print("Student added successfully")
    def add_teacher(self,name,subject):
        t=teacher(name,subject)
        self.teachers[subject]=t
        print("Teacher added successfully")
    def display_students(self):
        for rollno in self.students:
            self.students[rollno].display()
            print()
    def display_teachers(self):
        for subject in self.teachers:
            self.teachers[subject].display()
            print()
if __name__ == "__main__":
    s=school()
    while True:
        print("1.Add student")
        print("2.Add teacher")
        print("3.Display students")
        print("4.Display teachers")
        print("5.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            name=input("Enter student name:")
            rollno=random.randint(1000,9999)
            standard=input("Enter standard:")
            s.add_student(name,rollno,standard)
        elif choice==2:
            name=input("Enter teacher name:")
            subject=input("Enter subject:")
            s.add_teacher(name,subject)
        elif choice==3:
            s.display_students()
        elif choice==4:
            s.display_teachers()
        elif choice==5:
            break
        else:
            print("Invalid choice")
# Output:
