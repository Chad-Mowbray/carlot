from car import Car


class UsedCar(Car):

    def __init__(self, new, make, model, original_price, years_old):
        super().__init__(new, make, model, original_price, years_old)
        self.current_price = int(original_price) - (int(years_old) * 1000)

    def advertise(self):
        print(f"I'm only worth {self.current_price} and haven't had my oil changed in years")