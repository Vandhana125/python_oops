class Employee:
    company = "Google"   
    def __init__(self, emp_id, name, salary, address, role):
        self.id = emp_id
        self.name = name
        self.__salary = salary
        self.__address = address
        self.role = role
emp1 = Employee("G101", "John", 50000, "Bangalore", "Software Engineer")
print("Company:", emp1.company)
print("Employee ID:", emp1.id)
print("Name:", emp1.name)
print("Role:", emp1.role)