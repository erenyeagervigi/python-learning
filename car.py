class car:
    def __init__(self, model, year, colour, for_sale):
         self.model = model
         self.year = year
         self.colour = colour
         self.for_sale = for_sale

    def drive(self):
        print(f"the {self.model} is obviously driving!!")

    def stop(self):
        print(f"stop the fucking {self.model}!!")

    def describe(self):
        print(f"the car is {self.model} has a flashy {self.colour} and its from the year {self.year}")