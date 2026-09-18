# from abc import ABC, abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class CreditCardPayment(payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card.")
# class UPIpayment(payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using UPI.")
# payment1 = CreditCardPayment()
# payment1.pay(1000)
# payment2 = UPIpayment()
# payment2.pay(1000)


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