def describe_pet(pet_name, animal_type = "dog"):
    """Display informatin about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")
describe_pet("harry", "hamster")
describe_pet(pet_name = "harry", animal_type = "hamster")

print("-" * 50)

describe_pet(pet_name = "jimmy")
describe_pet("jimmy")
describe_pet(pet_name = "harry", animal_type = "hamster")

print("-" * 50)

# A dog named Willie.
describe_pet("Willie")
describe_pet(pet_name = "willie")

# A hamster named Harry.
describe_pet("harry", "hamster")
describe_pet(pet_name = "harry", animal_type = "hamster")
describe_pet(animal_type = "hamster", pet_name = "harry")

#describe_pet()