class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

print(Movie('The Matrix', 1994).name)

matrix = Movie('The Matrix', 1994)
print(matrix.name)

# Magic method

movies = ['Matrix', 'finding Nemo']
print(movies.__class__)
print("hi".__class__)
print(len(movies))

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    #this is more like code oriented representation
    def __repr__(self): # useful when we are running a debugger
        return f'<Garage {self.cars}' #repr is more important than str, so if we have to implement only one then implement repr

    #this is more like user oriented representation
    def __str__(self):  #if we don't define this method and we difine only repr then for print(object_of_Garage) repr gets executed
        return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")

print(len(ford))

print(ford[0]) # Garage.__getitem__(ford, 0)
print(ford)

for car in ford: # we can use for loop over Garage object only if dunder len and getitem methods are already defined as for loop is going to use both
    print(car)