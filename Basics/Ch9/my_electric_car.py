from car import ElectricCar

my_leaf = ElectricCar('chevrolet', 'volt', 2020)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()