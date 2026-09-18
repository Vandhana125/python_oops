# Encapsulation

# Definition:Encapsulation means wrapping data and methods together and protecting the data.

# Used for: Data protection.

# Real-time example:
# Bank account — you cannot directly change your bank balance; you use methods like deposit and withdraw.



class Person:
    def __init__(self, name, age):
        self.pname = name
        self.page = age
p1 = Person("john", 19)
print(p1.pname)
print(p1.page)