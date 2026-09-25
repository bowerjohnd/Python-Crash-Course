alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("-" * 50)

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    if alien_number < 10:
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    elif alien_number < 20:
        new_alien = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    else:
        new_alien = {'color': 'red', 'points': 15, 'speed': 'fast'}

    aliens.append(new_alien)

# Show every 5th aliens
for alien in aliens[::5]:
    print(alien)
print("...")


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show all aliens
for alien in aliens:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
