# Evan Cropper - fixed version
# clinic.py
# app will store cats and dogs within objects and has the capability of data storage for multiple pets

# define class Pet
class Pet():
    # initializer
    def __init__(self, name, age, weight, color, sex, temperament = 'calm', healthStatus = 'healthy', isVaccinated = False):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.sex = sex
        self.temperament = temperament
        self.healthStatus = healthStatus
        self.isVaccinated = isVaccinated
        
        
# define class Dog with super Pet
class Dog(Pet):
    # initializer
    def __init__(self, name, breed, age, weight, color, sex, note, temperament = 'calm', healthStatus = 'healthy', isVaccinated = False, isFixed = False):
        # init from superclass Pet
        super(Dog, self).__init__(name, age, weight, color, sex, temperament, healthStatus, isVaccinated)
        # make python realize there are variables within this class
        self.temperament = temperament
        self.healthStatus = healthStatus
        self.isVaccinated = isVaccinated
        self.isFixed = isFixed
        self.breed = breed
        self.note = note
        

# define class Cat with super Pet
class Cat(Pet):
    # initializer
    def __init__(self, name, breed, age, weight, color, sex, note, temperament = 'calm', healthStatus = 'healthy', isVaccinated = False, isFixed = False):
        # init from superclass Pet
        super(Cat, self).__init__(name, age, weight, color, sex, temperament, healthStatus, isVaccinated)
        # make python realize there are variables within this class
        self.temperament = temperament
        self.healthStatus = healthStatus
        self.isVaccinated = isVaccinated
        self.isFixed = isFixed
        self.breed = breed
        self.note = note
        
# create cute animals
barley = Dog("Barley", "Golden Retriever", 5, 70, 'yellow', 'male', "very good boi")
felix = Cat("Felix", "Shorthair", 2, 10, 'black', 'male', "feline fine")
bonbon = Dog("Bonbon", "Poodle", 3, 35, 'white', 'female', "you can carry her around like a backpack")
jumanji = Cat("Jumanji", "Tabby", 5, 9, 'orange', 'male', "out for blood")
list = [barley, felix, bonbon, jumanji]

# print list in nice format
print("---------------------")
for pet in list:
    print("Name:   ", pet.name)
    print("Breed:  ", pet.breed)
    print("Age:    ", pet.age, "years")
    print("Weight: ", pet.weight, "lbs")
    print("Sex:    ", pet.sex)
    print("Notes:  ", pet.note)
    print("---------------------")
