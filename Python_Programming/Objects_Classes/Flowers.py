class Flowers:

    def __init__(self, flower_name, num_pedals, price):
        self.flower_name = flower_name
        self.num_pedals = num_pedals
        self.price = price

    def name(self, new_name):
        self.flower_name = new_name

    def display_name(self):
        return self.flower_name

    def pedals(self, new_pedals):
        self.num_pedals = new_pedals

    def display_pedals(self):
        return self.num_pedals

    def price(self, new_price):
        self.price = new_price

    def display_price(self):
        return self.price


f1 = Flowers("sunflower", 10, 5)
print(f1.display_name())
f1.name("yellow")
print("New name: ", f1.display_name())

print("Price is: $", f1.price)
