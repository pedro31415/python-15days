class Car:
    def __init__(self, make, model, year, color): # constructor
        self.make = make # attribute
        self.model = model
        self.__year = year
        self.color = color
    
    def drive(self): 
        print("This car is driving")
    
    def stop(self):
        print("This car is stopped")

    @property
    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        self.__year = year

car_one = Car("ford", "mustang", 2024, "red")


print(car_one.get_year())
car_one.set_year(2025)
print(car_one.get_year())
    

