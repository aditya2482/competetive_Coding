from dataclasses import dataclass

@dataclass
class person:
    name:str
    age:int



@dataclass
class employee(person):
    prev = 0
    employee_dept:str = "intern"
    employee_id:int = prev
    
    @classmethod 
    def set_id(self):
        employee.prev = employee.prev+1
        return employee.prev
    
    def __post_init__(self):
        self.employee_id:int = self.set_id()
        return self.employee_id

    
    

e1 = employee("Aditya","23")
e2 = employee("sanju","32")
e3 = employee("kumar","12")
e4 = employee("acchint","23","QA-developer")

print(e4)




