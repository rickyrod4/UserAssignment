class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("\nUser:", self.name)
        print("Balance: $", self.account_balance)

    def transfer_money(self, otherUser, amount):
        self.make_withdrawal(amount)
        otherUser.make_deposit(amount)
        return self

#Creating Users and initial Deposits
ricky = User("Ricky Rodriguez", "ricardo.rodriguez@gmail.com")
christian = User("Christian Estrada","cjestrad@aol.com")
adam = User("Adam Renteria", "adam.renteria@yahoo.com")

#1st User
ricky.make_deposit(500).make_deposit(740).make_withdrawal(400).make_deposit(2500).display_user_balance()

#2nd User
christian.make_deposit(1000).make_withdrawal(250).make_deposit(2000).make_withdrawal(700).display_user_balance()

#3rd User
adam.make_deposit(2750).make_withdrawal(250).make_withdrawal(800).make_withdrawal(600).display_user_balance()

#transer Amount
ricky.transfer_money(adam, 500).display_user_balance
adam.display_user_balance()
