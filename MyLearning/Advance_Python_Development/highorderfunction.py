def greet():
    print("Hello")

def before_and_after(func):
    print('Before...')
    func()
    print('After...')

before_and_after(greet)
before_and_after(lambda : 5)


movies = [
    {'name': 'Run', 'Director': 'ABC'},
    {'name': 'Race', 'Director': 'XYZ'},
    {'name': 'Raaz', 'Director': 'PQR'}
]
def find_movie(expected, finder):
    for movie in movies:
        if expected ==finder(movie):
            return movie

find_by = input('What property you are searching for: ')
looking_for = input('What are you looking for.. ')

movie = find_movie(looking_for, lambda movie: movie[find_by])

print(movie or 'No Movies found!!!')
