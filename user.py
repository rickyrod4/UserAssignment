class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print("\nUser:", self.name)
        print("Balance: $", self.account_balance)

    def transfer_money(self, otherUser, amount):
        self.make_withdrawal(amount)
        otherUser.make_deposit(amount)

#Creating Users and initial Deposits
ricky = User("Ricky Rodriguez", "ricardo.rodriguez@gmail.com")
christian = User("Christian Estrada","cjestrad@aol.com")
adam = User("Adam Renteria", "adam.renteria@yahoo.com")

#1st User
ricky.make_deposit(500)
ricky.make_deposit(740)
ricky.make_withdrawal(400)
ricky.make_deposit(2500)
ricky.display_user_balance()

#2nd User
christian.make_deposit(1000)
christian.make_withdrawal(250)
christian.make_deposit(2000)
christian.make_withdrawal(700)
christian.display_user_balance()

#3rd User
adam.make_deposit(2750)
adam.make_withdrawal(250)
adam.make_withdrawal(800)
adam.make_withdrawal(600)
adam.display_user_balance()


#transer Amount
ricky.transfer_money(adam, 500)
ricky.display_user_balance()
adam.display_user_balance()
