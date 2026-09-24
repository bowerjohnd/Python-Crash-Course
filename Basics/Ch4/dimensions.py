dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250        # error, tuples are immutable

my_t = (3,)                 # tuple, of 1 element (needs the trailing comma)
my_other_t = (3)            # integer, not a tuple
print(my_t)
print(my_other_t)

print("-" * 50)

for dimension in dimensions:
    print(dimension)

print("-" * 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)         # writing over original, not changing immutable values
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
