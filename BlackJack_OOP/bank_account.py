class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} is deposited in {self.name}'s bank account.")
        else:
            print("Insufficient amount")
        self.get_balance()

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            print(f"The transaction is approved! Get your money - ${amount}")
            self.balance -= amount
        else:
            print("Insufficient amount")
        self.get_balance()

    def get_balance(self):
        print(f"Balance is ${self.balance}")


anton_bank_account = BankAccount("Anton", 0)
anton_bank_account.deposit(-1)
anton_bank_account.withdraw(100)
