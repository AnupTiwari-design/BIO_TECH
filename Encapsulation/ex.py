class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
ob=BankAccount(1000)
ob.deposit(100)
ob.withdraw(500)
print(ob.get_balance())
    


