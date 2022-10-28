class Account:
    acc_id = 1    
    def __init__(self,name,age,balance):
        self.name = name
        self.age = age
        self.balance = balance

        self.account_id = Account.acc_id
        self.acc_id += 1

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

acc_1 = Account('Debakor',24,16000)
acc_2 = Account('Joy',25,500)
print(acc_2.acc_id)
print(acc_2.balance)
acc_2.deposit(500)
print(acc_2.balance)
acc_2.withdraw(300)
print(acc_2.balance)