import datetime as dt


class BikeRental:
    def __init__(self, stock=0):
        self.__stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock

    def show_stock(self):
        print(f"Currently available {self.stock} bikes")
        return self.stock

    def rent_bike_on_hourly_basis(self, number_bikes):
        if number_bikes <= 0:
            print("Incorrect number of bikes")
            return None
        elif number_bikes > self.stock:
            print(f"Sorry! In this moment available only {self.stock} bikes")
            return None
        else:
            now = dt.datetime.now()
            print(f"You rent {number_bikes} bike/s today at {now.hour}:{now.minute}:{now.second}, on hourly basis")
            print("The price would be $5 for one bike per hour")
            self.stock -= number_bikes
            return now

    def rent_bike_on_daily_basis(self, number_bikes):
        if number_bikes <= 0:
            print("Incorrect number of bikes")
            return None
        elif number_bikes > self.stock:
            print(f"Sorry! In this moment available only {self.stock} bikes")
            return None
        else:
            now = dt.datetime.today()
            print(f"You rent {number_bikes} bike/s today on {now}, on daily basis")
            print("The price would be $20 for one bike per day")
            self.stock -= number_bikes
            return now

    def rent_bike_on_weekly_basis(self, number_bikes):
        if number_bikes <= 0:
            print("Incorrect number of bikes")
            return None
        elif number_bikes > self.stock:
            print(f"Sorry! In this moment available only {self.stock} bikes")
            return None
        else:
            now = dt.datetime.today()
            print(f"You rent {number_bikes} bike/s today on {now}, on weekly basis")
            print("The price would be $60 for one bike per week")
            self.stock -= number_bikes
            return now

    def return_bike(self, request):
        time_rental, rental_basis, number_bikes = request
        bill = 0
        if time_rental and rental_basis and number_bikes:
            self.stock += number_bikes
            now = dt.datetime.now()
            rental_period = now - time_rental
            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * number_bikes
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * number_bikes
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * number_bikes
            if 3 <= number_bikes <= 6:
                print("You have a discount 30%")
                bill = bill * 0.7
            print(f"Your total bill would be: {bill}")
            return bill
        else:
            print("Is this bike from our service ?")
            return None
