class Car:
    def __init__(self, make, model, year, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.available = available

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Customer:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number

    def __str__(self):
        return f"{self.name} (License: {self.license_number})"


class RentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rented_cars = {}

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def rent_car(self, customer, car):
        if car.available:
            car.available = False
            self.rented_cars[customer] = car
            return f"{customer.name} rented {car}."
        else:
            return "Sorry, the car is not available for rent."

    def return_car(self, customer):
        if customer in self.rented_cars:
            returned_car = self.rented_cars.pop(customer)
            returned_car.available = True
            return f"{customer.name} returned {returned_car}."
        else:
            return f"{customer.name} did not rent any car."


def simulate_conversation():
    rental_system = RentalSystem()

    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("Honda", "Civic", 2021)
    car3 = Car("Ford", "Mustang", 2020)

    customer1 = Customer("John Doe", "AB123456")
    customer2 = Customer("Jane Smith", "CD789012")

    rental_system.add_car(car1)
    rental_system.add_car(car2)
    rental_system.add_car(car3)

    rental_system.add_customer(customer1)
    rental_system.add_customer(customer2)

    print("Owner: Welcome to the Car Rental System!")

    while True:
        action = input("\nCustomer: What would you like to do? (rent/return/exit): ").lower()

        if action == 'exit':
            print("Owner: Thank you for using our Car Rental System. Have a great day!")
            break

        elif action == 'rent':
            customer_name = input("Customer: Please enter your name: ")
            license_number = input("Customer: Please enter your license number: ")

            customer = Customer(customer_name, license_number)

            available_cars = [car for car in rental_system.cars if car.available]
            if not available_cars:
                print("Owner: Sorry, there are no cars available for rent at the moment.")
                continue

            print("Owner: Here are the available cars:")
            for i, car in enumerate(available_cars, 1):
                print(f"{i}. {car}")

            car_index = int(input("Customer: Please enter the number of the car you want to rent: ")) - 1

            if 0 <= car_index < len(available_cars):
                selected_car = available_cars[car_index]
                result = rental_system.rent_car(customer, selected_car)
                print(f"Owner: {result}")
            else:
                print("Owner: Invalid car selection. Please try again.")

        elif action == 'return':
            customer_name = input("Customer: Please enter your name: ")
            license_number = input("Customer: Please enter your license number: ")

            customer = Customer(customer_name, license_number)
            result = rental_system.return_car(customer)
            print(f"Owner: {result}")

        else:
            print("Owner: Invalid action. Please enter 'rent', 'return', or 'exit'.")

# Run the conversation simulation
simulate_conversation()
