# Class 1
class Student:
    overall_total = 0

    def __init__(self):  # use of __init__ method
        self.full_name = input('Student Name: ')
        self.rollno = input('Roll No: ')
        Student.overall_total += 1

    def count(self):    # Defining a function inside a class
        print('No. of students enrolled are ', Student.overall_total)

    def display(self):
        print('Student Name is ', self.full_name)
        print('Roll No. is ', self.rollno)


# Class 2

class TransferStudent(Student):

    def __init__(self):
        super(TransferStudent, self).__init__()  # use of super() call
        self.TransferredCredits = input('No. of credits that are transferred')


class System:  # Class #3

    def __init__(self):
        self.TypeOfSystem = input('System Online (or) InClass: ')

    def display(self):
        print('The system the student enrolled is: ', self.TypeOfSystem)


class Grades(TransferStudent):  # Class #4

    def __init__(self, grade, credits):
        TransferStudent.__init__(self)  # Another way of inheriting the parent class
        self.Grades = grade
        self.EnrolledCredits = credits

    def TotalCredits(self):
        self.TotalCreditsEnrolled = self.TransferredCredits + credits
        print('Total no. of credits completed: ', self.TotalCreditsEnrolled)

    def display(self):
        print('Student Name is ', self.full_name)
        print('Roll No. is ', self.rollno)
        print('Transferred credits are: ', self.TransferredCredits)
        print('Total number of credits enrolled: ', self.EnrolledCredits)
        print('Grade obtained is: ', self.Grades)


class Attendance:  # Class #5

    def __init__(self, percentage):
        self.__attendance = percentage  # Declaration of the private data member
        if self.__attendance < 65:
            print("Student's attendance is low")


# Creating and calling all the classes

Student_1 = Student()

Student_2 = TransferStudent()
Student_3 = TransferStudent()

Student_4 = Grades("B-", "25")
Student_5 = Grades("C", "90")

Student_6 = Attendance(84)

Student_5.display()

Student_3.display()

Student_5.count()
Student_1.display()
