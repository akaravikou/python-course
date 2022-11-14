import random
from BlackJack_OOP.inheritance.person import Person


class Customer(Person):
    def __init__(self, name):
        super().__init__(name= name, phone="962", address="Minsk")
        self.customer_id = random.randint(1, 100)

    def purchase(self, item):
        print(f"{item}, has been purchased")


new_customer = Customer("Nomad")
print(new_customer.name, new_customer.customer_id)