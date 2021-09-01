import json

'''
json data is very much like a dictionary
the json library help us to convert the json data to a dictionary easily
'''

file = open('friends_json.txt', 'r')
file_contents = json.load(file)     #read files and turns it to a dictionary

file.close()

print(file_contents)
print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)      #loads is used to read a json string into a dictionary
print(incorrect_car[0]['name'])

correct_car = json.dumps(incorrect_car)     #dumps is used to load a dictionary as a string
print(type(correct_car))    #json allows us to use list or dictionary, not tuples