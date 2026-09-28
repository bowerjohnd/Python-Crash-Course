import pizza_module as pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('-' * 50)

from pizza_module import make_pizza

make_pizza(16, 'pepperoni', 'sausage', 'bacon')
make_pizza(12, 'mushrooms', 'green peppers', 'olives')

print('-' * 50)

from pizza_module import make_pizza as mp

mp(16, 'hot dogs', 'ketchup', 'mustard')
mp(12, 'shwarma', 'falafel', 'feta cheese')

print('-' * 50)

import pizza_module as p

p.make_pizza(16, 'hot dogs', 'ketchup', 'mustard')
p.make_pizza(12, 'shwarma', 'falafel', 'feta cheese')

print('-' * 50)

from pizza_module import *

make_pizza(16, 'hot dogs', 'ketchup', 'mustard')
make_pizza(12, 'shwarma', 'falafel', 'feta cheese')
