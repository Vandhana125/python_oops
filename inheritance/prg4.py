# Inheritance :

# Definition:
# Inheritance means a child class gets properties and methods from a parent class.

# Used for: Code reuse.

# Real-time example:
# Dog is an Animal. Dog can use the methods of Animal.




class Order:
    def f1(self):
        print("f1 method of order class")

class Customer(Order):
    def f1(self):
        print("f1 method of customer class")


c=Customer()
c.f1()


class Order:
    def __init__(self,order_id):
        self.__order_id=order_id

class Customer(Order):
    def __init__(self, order_id):
        super().__init__(order_id)   # super is used to call a parent class
        print("customer class constructor")

c=Customer(1000)
print(Customer.mro())




# Multiple inheritance

class SBI:
    def discount(self):
        print("SBI gives 10% discount")


class HDFC:
    def discount(self):
        print("HDFC gives 15% discount")


class emp(SBI, HDFC):
    print("Both SBI and HDFC")


s = SBI()
h = HDFC()
e1 = emp()

s.discount()
h.discount()
e1.discount()




# Create a Python program to demonstrate multiple inheritance and polymorphism using bank discount systems.

# Create an SBI class that gives a 10% discount.
# Create an HDFC class that gives a 15% discount.
# Create an Emp class that inherits from both SBI and HDFC.
# Create objects for SBI, HDFC, and Emp.
# For an amount of ₹1000, calculate and display the discount and final amount for SBI and HDFC.



class SBI:
    def discount(self, amount):
        return amount * 10 / 100


class HDFC:
    def discount(self, amount):
        return amount * 15 / 100


class Emp(SBI, HDFC):
    pass


s = SBI()
h = HDFC()
e1 = Emp()

amount = 1000

print("SBI Discount:", s.discount(amount))
print("SBI Final Amount:", amount - s.discount(amount))

print("HDFC Discount:", h.discount(amount))
print("HDFC Final Amount:", amount - h.discount(amount))


# Create a Python program using OOP concepts for an employee salary system.

# Create an Employee class with ID, Name, and Salary.
# Create an Insurance class with Policy Number and deduct 15% of salary.
# Create an EMI class with EMI ID and deduct 10% of salary.
# Create details for 3 employees: X, Y, and Z.
# Calculate and display the total deduction and remaining salary for each employee.



class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary


class Insurance(Employee):
    def __init__(self, id, name, salary, policy_no):
        super().__init__(id, name, salary)
        self.policy_no = policy_no

    def deduction(self):
        return self.salary * 15 / 100


class EMI(Employee):
    def __init__(self, id, name, salary, emi_id):
        super().__init__(id, name, salary)
        self.emi_id = emi_id

    def deduction(self):
        return self.salary * 10 / 100


# 3 Employees
e1 = Employee(101, "X", 30000)
e2 = Employee(102, "Y", 40000)
e3 = Employee(103, "Z", 50000)

# Insurance
i1 = Insurance(101, "X", 30000, 1)
i2 = Insurance(102, "Y", 40000, 2)
i3 = Insurance(103, "Z", 50000, 3)

# EMI
emi1 = EMI(101, "X", 30000, 101)
emi2 = EMI(102, "Y", 40000, 102)
emi3 = EMI(103, "Z", 50000, 103)


# Display
for e, i, emi in [(e1, i1, emi1),(e2, i2, emi2),(e3, i3, emi3)]:

    insurance = i.deduction()
    emi_amount = emi.deduction()
    total = insurance + emi_amount
    remaining = e.salary - total

    print("\nEmployee ID:", e.id)
    print("Name:", e.name)
    print("Salary:", e.salary)
    print("Policy No:", i.policy_no)
    print("Insurance 15%:", insurance)
    print("EMI ID:", emi.emi_id)
    print("EMI 10%:", emi_amount)
    print("Total Deduction:", total)
    print("Remaining Salary:", remaining)