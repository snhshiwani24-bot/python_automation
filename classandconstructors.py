# class A:
#     a=22
#     def m():
#         print("shiwani")
# print(A.a)
# A.m()

# class A:
#     a=22
#     def m(self):
#         print("shiwani")

# obj=A()
# print(obj.a)
# obj.m()

# class Car:
#     wheels=4
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#         print(self.brand,self.model)
#    def display_info(self):
#         print(f"{self.brand} {self.model} has {self.wheels} wheels")

# my_car=Car("Toyota","Corolla")
# my_car.display_info()

# Given Input: Starting balance of 1000, deposit 500, withdraw 200, then attempt to withdraw 2000.

# Expected Output:

# Balance after deposit: 1500
# Balance after withdrawal: 1300
# Insufficient funds. Current balance: 1300

class Account_Transaction:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance +=amount
        print(f"balance after deposit: {self.balance}")
    def withdraw(self, amount):
        if amount<= self.balance:
            self.balance -= amount
            print(f"balance after withdrawal: {self.balance}")
        else:
            print(f"Insufficient funds. current balance: {self.balance}")
account = Account_Transaction(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)

           



