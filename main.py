from pet import Pet

my_pet = Pet("Buddy")
print(f"Start energy: {my_pet.energy_level}")

my_pet.feed_pet()
print(f"After feeding: {my_pet.energy_level}")

my_pet.play_with_pet()
print(f"After playing: {my_pet.energy_level}")