

class Car:
    def __init__(self, year=2020, manufacturer='', model='', mileage=0, fuel_consumption=0.0):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = mileage
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'{self.year} {self.manufacturer} {self.model}, Пробіг: {self.mileage} км, Витрата палива: {self.fuel_consumption} л/100км'



car1 = Car(year=2021, manufacturer='Toyota', model='Corolla', fuel_consumption=6.5)
car2 = Car(year=2019, manufacturer='Honda', model='Civic', fuel_consumption=5.8)
car3 = Car(manufacturer='Ford', model='Focus', fuel_consumption=7.2)


print(car1)
print(car2)
print(car3)
