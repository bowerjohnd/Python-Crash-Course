cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()                             # permanent sort
print(cars)
cars.sort(reverse=True) 
print(cars)

print("-" * 50)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))                     # temporary sort

print("\nHere is the original list again:")
print(cars)

print("-" * 50)

print(cars)
cars.reverse()
print(cars)

print(len(cars))

