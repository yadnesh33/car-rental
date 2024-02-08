car1 = {"id": 1, "brand": "BMW", "rent": 20, "available": True}
car2 = {"id": 2, "brand": "Mercedes", "rent": 30, "available": True}
car3 = {"id": 3, "brand": "Audi", "rent": 40, "available": True}

cars = {"car1": car1, "car2": car2, "car3": car3}
customers = []
earnings = 0

while True:
    print("\nWelcome to the Car Rental Shop!")
    print("Please select an option:")
    print("1. View available cars")
    print("2. Rent a car")
    print("3. Show Customers Information")
    print("4. Show earnings")
    print("5. Return Car")
    print("6. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        print("\nAvailable cars:")
        for i, car in cars.items():
            if car["available"]:
                print(f"Car ID: {car['id']}, Brand: {car['brand']}, Hourly Rate: ₹{car['rent']}")

    elif option == 2:
        car_id = int(input("Enter car ID: "))
        hours = int(input("For how many hours do you want to rent the car? "))

        for car_name, car in cars.items():
            if car["id"] == car_id and car["available"]:
                name = input("Enter your name:")
                customer_info = {
                    "c_name": name,
                    "car_id": car["id"],
                    "rented_car": car["brand"],
                    "hours": hours,
                    "bill_amount": hours * car["rent"]
                }
                customers.append(customer_info)
                print(f"{name} has rented a car for {hours} hours. Your Bill Amount: ₹{customer_info['bill_amount']}")
                car["available"] = False
                earnings= earnings+ customer_info['bill_amount']
                break
        else:
            print("Car not available.")

    elif option == 3:
        print("\nCustomers Information:")
        for customer in customers:
            print(f"Customer Name: {customer['c_name']}, Car ID: {customer['car_id']}, Rented Car: {customer['rented_car']}, Hours: {customer['hours']}, Bill Amount: ₹{customer['bill_amount']}")

    elif option == 4:
        print(f"Total earnings: ₹{earnings}")
        
    elif option == 5:
        return_id= int(input("Enter Car ID you want to retun:"))
        for car_name, car in cars.items():
            if return_id == car["id"] and not car['available']:
                customers.remove(customer)
                car['available']= True
                print("Car returned Successfully.")
                break
            else:
                print("Car not returned.")

    elif option == 6:
        print("Thank You for using our services.")
        break

# Run the conversation simulation
simulate_conversation()
