class Vehicle:
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_vehicle_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    def start(self):
        print(f"The {self.brand} {self.model} is starting...")

class Car(Vehicle): #car ingerits from vehicle
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year) #call parent's constructor
        self.num_doors = num_doors

    def drive(self):
        print(f"The {self.brand} {self.model} is driving away with {self.num_doors} doors!")

     #Method overriding : car has its own specific start message
    def start(self):
        print(f"The {self.brand} {self.model} is starting with a roar!")

class Motorcycle(Vehicle): #motorcycle ingerits from vehicle
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def ride (self):
        sidecar_status = "With a sidecar" if self.has_sidecar else "Without a slidecar"
        print(f"The {self.brand} {self.model} is riding {sidecar_status}")


# Create instances of inherited classes
my_car = Car("Toyota", "Camry", 2020, 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, False)


print("\n--- Car Informatin(Ingerited) ---")
my_car.display_vehicle_info()
my_car.start()
my_car.drive()

print("\n--- Motorcycle Information(Ingerited) ---")
my_motorcycle.display_vehicle_info()
my_motorcycle.start()   
my_motorcycle.ride()



# A function that can take any Vehicle object
def perform_start_sequence(vehicle):
    print(f"\nInitiating start sequence for {vehicle.brand} {vehicle.model}..")
    vehicle.start() # This calls the appropriate start method for the object's type
    if isinstance(vehicle, Car):
        vehicle.drive()
    elif isinstance(vehicle, Motorcycle):
        vehicle.ride()

# create a generic vehicle (no specific child class)
generic_vehicle = Vehicle("Generic", "Transporter", 2023)

# Create new instances for clarity
my_car_poly = Car("Tesla", "MOdel 3", 2022, 4)
my_motorcycle_poly = Motorcycle("Ducati", "Monster", 2021, False)

#Call the function with different types of object
perform_start_sequence(generic_vehicle)
perform_start_sequence(my_car_poly)
perform_start_sequence(my_motorcycle_poly)

# Another example of polymorphism with a list of vehicles
vehicles = [generic_vehicle, my_car_poly, my_motorcycle_poly]

print("\n--- Demostarting polymorphism in loop ---")
for vehicle in vehicles:
    vehicle.display_vehicle_info() #common method froom base class
    vehicle.start() #polymorphic method call
    print("------------")


