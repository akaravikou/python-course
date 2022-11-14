class Person:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone_number = phone
        self.address = address

    def update_contact(self, new_number):
        self.phone_number = new_number
        print(f"The phone number has been updated to {self.phone_number}")

