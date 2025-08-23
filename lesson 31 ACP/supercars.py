class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "300 km/h"
def car_details(car):
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
bmw_car = BMW()
ferrari_car = Ferrari()
print("BMW Details:")
car_details(bmw_car)
print("Ferrari Details:")
car_details(ferrari_car)
