from pet import Pet

my_pet = Pet("Buddy")
print(f"Before feeding: {my_pet.energy_level}")

my_pet.feed_pet()
print(f"After feeding: {my_pet.energy_level}")