import csv
from newcar import NewCar
from usedcar import UsedCar

class Carlot:

    def __init__(self):
        self.inventory = self.get_inventory()

    def get_inventory(self):
        cars = []
        with open('inventory.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                car = None
                if row["new"] == 'true':
                    car = NewCar(**dict(row))
                else:
                    car = UsedCar(**dict(row)) 
                cars.append(car)     
        return cars

    def hold_sale(self):
        for car in self.inventory:
            car.advertise()