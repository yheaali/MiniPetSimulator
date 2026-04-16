<<<<<<< HEAD
class Pet:
    def __init__(self, name):
        self.name = name
        self.energy_level = 50 
<<<<<<< HEAD
        def play_with_pet(self):
=======
            def feed_pet(self):
        self.energy_level += 20
        print(f"{self.name} is eating! Energy +20") 
            def play_with_pet(self):
>>>>>>> ff0bb7d18d60f2fef62e01b459db2134a9d6e983
=======
    def feed_pet(self):
        self.energy_level += 20
        print(f"{self.name} is eating! Energy +20")
    
    def play_with_pet(self):
>>>>>>> 2257e0e7e55783879f0b0fd3ea15912d5dd0fbb2
        self.energy_level -= 15
        print(f"{self.name} is playing! Energy -15")