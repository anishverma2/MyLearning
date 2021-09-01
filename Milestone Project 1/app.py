movies = []

def add_movies():
    title = input ("Enter the movie title: ")
    director = input ("Enter the director name: ")
    release_year = input ("Enter the release year: ")

    movies.append({
        "Title": title,
        "Director" : director,
        "Release_Year" : release_year
    })

def list_movies():
    for movie in movies:
        print(movie)

def search_movie():
    search_input = int(input(''''\n Enter 1 if you want to search for a director and his movies
    2 if you want to search a movie with its title
    3 if you want to search a movie with its release date:\n'''))

    if search_input == 1:
        user_response = input("Enter the director Name: ")
        for movie in movies:
            if user_response == movie['Director']:
                print (movie)
        return
    elif search_input == 2:
        user_response = input("Enter the movie name: ")
        for movie in movies:
            if user_response == movie['Title']:
                print (movie)
        return
    elif search_input == 3:
        user_response = input("Enter the Release year: ")
        for movie in movies:
            if user_response == movie['Release_Year']:
                print (movie)
        return
    else:
        print("Wrong input entered!!!")
        return

user_input = '''\nEnter your response 
'a' to add a movie 
'l' to list all the movies
's' to search for a movie 
'q' to quit this program:\n'''

response = input(user_input)

while response != 'q':
    if response == 'a':
        add_movies()
    elif response == 'l':
        list_movies()
    elif response == 's':
        search_movie()
    else:
        print('''Wrong input Entered!!!
        Please enter Again!!!''')
    response = input(user_input)

print("Out of the program")