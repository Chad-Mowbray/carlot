from car import Car

class NewCar(Car):

    def __init__(self, new, make, model, original_price, years_old):
        super().__init__(new, make, model, original_price, years_old)
        self.new_car_smell = True
    
    def advertise(self):
        super().advertise()
        print("and I smell new")