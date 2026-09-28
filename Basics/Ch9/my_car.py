from car import Car

my_new_car = Car('ford', 'mustang', 1998)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 99
my_new_car.read_odometer()