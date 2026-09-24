my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]              # copy of my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("-")

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

copy_list = my_foods                   # reference to my_foods
copy_list.append('ghost pepper')       # change one and
print(my_foods)                        #
my_foods.append('jalapeno pepper')     # the other changes too
print(copy_list)                       #

