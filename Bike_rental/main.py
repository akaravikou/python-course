import bike_rental
import customer

rental = bike_rental.BikeRental(100)
customer = customer.Customer()

while True:
    print("""
    ============Bike Rental Service============
    1. Show available bikes
    2. Request a bike on hourly basis - $5
    3. Request a bike on daily basis - $20
    4. Request a bike on weekly basis - $60
    5. Return a bike/s
    6. Exit""")

    user_choice = input("Enter number operation please:")
    try:
        user_choice = int(user_choice)
    except ValueError:
        print("Incorrect value")
        continue
    if user_choice == 1:
        rental.show_stock()
    elif user_choice == 2:
        requested_bikes = customer.request_bike()
        rental_time = rental.rent_bike_on_hourly_basis(requested_bikes)
        customer.rental_time = rental_time
        customer.rental_basis = 2
    elif user_choice == 3:
        customer.rental_time = rental.rent_bike_on_daily_basis(customer.request_bike())
        customer.rental_basis = 3
    elif user_choice == 4:
        customer.rental_time = rental.rent_bike_on_weekly_basis(customer.request_bike())
        customer.rental_basis = 4
    elif user_choice == 5:
        request_tuple = customer.return_bike()
        bill = rental.return_bike(request_tuple)
        customer.bill = bill
        customer.rental_basis, customer.rental_time, customer.number_bikes = 0, 0, 0
    elif user_choice == 6:
        break
    else:
        print("Invalid value")
print("Thanks for using our rental-service")


