# Polymorphism

# Definition:
# Polymorphism means one method name can have different behavior.

# Used for: Same operation with different implementations.

# Real-time example:
# SBI and HDFC both provide discounts, but the discount can be different.



class SBI:
    def discount(self):
        print("SBI gives 5% discount")

class HDFC:
    def discount(self):
        print("HDFC gives 7% discount")

s = SBI()
h = HDFC()

s.discount()
h.discount()