"""
Ronan Ballantine
Bank Account Class
21/02/2022
"""
class Account:

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            print('\nNot a valid, positive amount')
        else:
            self.balance += deposit_amount
            print(f'\nNew balance: {self.balance}')

    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print('\nWithdrawal amount exceeds available funds')
        else:
            self.balance -= withdraw_amount
            print(f'\nWithdrawal Accepted')

    def __str__(self):
        return f'Account holder: {self.owner}\nAccount Balance: {self.balance}'

# Test account
account1 = Account('Max',400)

# Test __str__ method
print(account1)

# Test deposit method
account1.deposit(50)

# Test withdraw method with valid amount
account1.withdraw(75)

# Test withdraw method with invalid amount
account1.withdraw(500)
