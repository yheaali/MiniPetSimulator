from pet import Pet

my_pet = Pet("Buddy")
print(f"Before playing: {my_pet.energy_level}")

my_pet.play_with_pet()
print(f"After playing: {my_pet.energy_level}")