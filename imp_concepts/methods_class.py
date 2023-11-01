from datetime import date as dt

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # static method
    @staticmethod
    def isAdult(self,age):
        if self.age > 18:
            return True
        else:
            return False

    # class-method - Access class variable
    @classmethod
    def emp_from_year(emp_class, name, year):
        return emp_class(name, dt.today().year - year)
   
    def __str__(self):
        return 'Employee Name: {} and Age: {}'.format(self.name, self.age)
      
    #   instance-method
    def return_details(self):
        pass


e1 = Employee('Dhiman', 25)
print(e1)
e2 = Employee.emp_from_year('Subhas', 1987)
print(e2)
print(Employee.isAdult(25))
print(Employee.isAdult(16))