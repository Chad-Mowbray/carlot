class Car:

    def __init__(self, new, make, model, original_price, years_old):
        self.is_new = new
        self.make = make
        self.model = model
        self.original_price = original_price
        self.years_old = years_old

    def advertise(self):
        print(f"I'm a {self.make} and I cost {self.original_price} dollars")