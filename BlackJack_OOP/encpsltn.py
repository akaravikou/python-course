class Customer:

    def __init__(self, name, balance, contract_number):
        self.name = name
        self.set_balance(balance)
        self._contract_number = contract_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance < 0:
            self.__balance = 0
        elif balance > 10000:
            self.__balance = 10000
        else:
            self.__balance = balance

    def show_detail(self):
        print(f"Name: {self.name},"
              f"Contract number: {self.contract_number}")

    def show_balance(self):
        print(f"{self.name}'s balance: {self.balance}")


customer01 = Customer("Anton", 1000, "DF-002")
customer01.show_detail()
customer01.show_balance()
