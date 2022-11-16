class Customer:
    def __init__(self):
        self.__number_bikes = 0
        self.__rental_basis = 0
        self.__rental_time = 0
        self.__bill = 0

    @property
    def number_bikes(self):
        return self.__number_bikes

    @number_bikes.setter
    def number_bikes(self, number_bikes):
        self.__number_bikes = number_bikes

    @property
    def rental_basis(self):
        return self.__rental_basis

    @rental_basis.setter
    def rental_basis(self, rental_basis):
        self.__rental_basis = rental_basis

    @property
    def rental_time(self):
        return self.__rental_time

    @rental_time.setter
    def rental_time(self, rental_time):
        self.__rental_time = rental_time

    @property
    def bill(self):
        return self.__bill

    @bill.setter
    def bill(self, bill):
        self.__bill = bill

    def request_bike(self):
        number_bikes = input("How many bikes would you like to rent?")
        try:
            number_bikes = int(number_bikes)
        except ValueError:
            print("Incorrect value was entered")
            return -1
        if number_bikes < 1:
            print("Incorrect value was entered")
            return -1
        else:
            self.number_bikes = number_bikes
        return self.number_bikes

    def return_bike(self):
        if self.number_bikes and self.rental_basis and self.rental_time:
            return self.rental_time, self.rental_basis, self.number_bikes
        else:
            return 0, 0, 0

