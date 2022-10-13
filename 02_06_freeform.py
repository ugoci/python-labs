# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...


class BankAccount():

    def __init__(self, name, date, balance):
        self.name = name
        self.date = date
        self.balance = balance 
#add a string method to this class 

    def current_account(self, balance):
        current_balance = balance * 0.70
        print("current account balance is:",current_balance)

    def savings_account(self, balance):
        saving_balance = balance * 0.30
        print(f"savings account balance:", saving_balance)

    def transfer(self, transfer_amount):
        self.transfer_amount = transfer_amount
        print(f"{self.name} has transferred {transfer_amount} to an external account")
        self.balance = self.balance - self.transfer_amount
        print(f"{self.name}'s new account balance is {self.balance}")

    def loan(self, loan_amount):
        self.loan_amount = loan_amount
        print(f"{self.name} has just received a loan of {loan_amount}")
        self.balance = self.balance + self.loan_amount
        print(f"{self.name}'s new account balance is {self.balance}") 

class InsuranceCompany(BankAccount):

    def __init__ (self, premium, ceiling):
        self.premium = premium 
        self.ceiling = ceiling
        #print(f"pay a monthly insurance premium of {self.premium}")


jon = BankAccount("Jon", "Sept 9 2022", 100)
aviva = InsuranceCompany(35, 10000)

jon.current_account(100)
#print(jon.date)
print(jon.balance)
jon.transfer(20)
jon.loan(600)
#print(aviva.premium)
