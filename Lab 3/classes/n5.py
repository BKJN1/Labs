class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied. Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

acct1 = Account("John Doe", 1000)

print(acct1)

acct1.deposit(500)
acct1.deposit(200)

acct1.withdraw(300)
acct1.withdraw(1500)  
acct1.withdraw(-50)  

print(acct1)
