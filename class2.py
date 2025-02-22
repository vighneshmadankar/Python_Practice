class Student:
    name = "karan"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding New Student to Database ....")

s1 = Student("karan", 99)



print(s1.name, s1.marks)