movies = []


def add_movie():
    title = input("Enter the movie title: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'year': year
    })


def list_movie():
    for m in movies:
        print(m)


def find_movie():
    t = input("Enter the title of the movie")
    for m in movies:
        if m['title'] == t:
            print(m)
            return
    print(f"{t} movie not stored yet in the list")


MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
user_input = input(MENU_PROMPT)

while user_input != 'q':
    if user_input == 'a':
        add_movie()
    elif user_input == 'l':
        list_movie()
    elif user_input == 'f':
        find_movie()
    else:
        print("Wrong input entered!!! Please enter again")
    user_input = input(MENU_PROMPT)
