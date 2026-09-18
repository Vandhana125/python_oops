# Abstraction

# Definition:
# Abstraction means hiding unnecessary/internal details and showing only what is needed.

# Used for: Making complex systems easier to use.

# Real-time example:
# ATM — you enter PIN, select withdrawal, and get money. You don't need to know how the bank's internal system processes the transaction.


from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")
class UPIpayment(payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")
payment1 = CreditCardPayment()
payment1.pay(1000)
payment2 = UPIpayment()
payment2.pay(1000)



# Create a Python program using abstract class for sending notifications.

# Create an abstract class Notification.
# Create an abstract method send().
# Create three classes: SMS, Email, and WhatsApp.
# Each class should implement the send() method.
# Send the message "Your order has been received" through SMS, Email, and WhatsApp.

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class SMS(Notification):
    def send(self, message):
        print("SMS sent:", message)


class Email(Notification):
    def send(self, message):
        print("Email sent:", message)


class WhatsApp(Notification):
    def send(self, message):
        print("WhatsApp message sent:", message)


sms = SMS()
email = Email()
whatsapp = WhatsApp()

sms.send("Your order has been received")
email.send("Your order has been received")
whatsapp.send("Your order has been received")
