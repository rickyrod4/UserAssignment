class BankAccount:
    def __init__ (self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient Funds, Your account will be charged $5")
            self.balance -= 5


    def display_account_info(self):
        print(f"Balance: ${self.balance}\n")
        return self

    def yield_interest(self):
        self.balance = round(self.balance*(1+self.int_rate),2)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
    
    def display_user_balance(self):
        print("\nUser:", self.name)
        print("Balance: $", self.account.display_account_info())


#Creating Users
ricky = User("Ricky Rodriguez", "ricardo.rodriguez@gmail.com")
christian = User("Christian Estrada","cjestrad@aol.com")
adam = User("Adam Renteria", "adam.renteria@yahoo.com")

ricky.account.deposit(1000)
print(ricky.account.display_account_info())

#Creating Two Accounts
checking = BankAccount(int_rate=.01,balance= 1000)
saving = BankAccount(.025)


#1st Account
checking.deposit(500).deposit(750).deposit(2500).withdrawal(1000).yield_interest().display_account_info()

#2nd Account
saving.deposit(5000).deposit(2500).withdrawal(1000).withdrawal(750).withdrawal(2000).withdrawal(500).yield_interest().display_account_info()


#Testing New Users
print(christian.name)
christian.account.deposit(500).display_account_info()