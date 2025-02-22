# Employee 

class Employee:
    def  __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("Roll = ", self.role)
        print("department is ", self.department)
        print("salary is ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "1100000")

"""yeusuf = Employee("analyst", "Data", "100000")
yeusuf.showdetails()"""

engi1 = Engineer("Elon Musk", 40)
engi1.showdetails()
