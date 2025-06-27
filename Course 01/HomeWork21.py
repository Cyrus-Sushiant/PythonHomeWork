class Animal():
    zoo_name = ''
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def info(self):
        print(f"{self.name} {self.age}")

    def __str__(self):
        return f"{self.name} {self.age}"

class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"sound bird: {self.sound}")

lion = Animal("Lion", "Cat", 2, "hooooo")
print(lion.name, lion.species, lion.age, lion.sound)
lion.make_sound()
lion.info()
print(lion)

print()

bird = Bird("Sparrow", "Small", 1, "jik jik", "10 cm")
print(bird.name, bird.species, bird.age, bird.sound, bird.wing_span)
bird.make_sound()
bird.info()
print(bird)