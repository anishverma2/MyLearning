import csv

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"},
]

def write_to_file(*output):
    with open('file.csv', 'w', newline='') as f:
        writer = csv.writer(f)  #csv module takes care of comma and other special character also of the data
        f.write('name,director\n')
        print(output)
        out = list(output)
        print(out)
        for o in out:
            #name = [o for o in out.values()]
            o = tuple(o)
            print(type(o))
            print(o)
            writer.writerow(o)

        '''writer = csv.DictWriter(f, fieldnames=["name", "director"])
        writer.writeheader()
        writer.writerows(output)'''


def read_from_file():
    with open('file.csv', 'r') as f:
        '''reader = csv.reader(f)
        for line in reader:
            print(f"Name: {line[0]}\tDirector: {line[1]}")
        '''


        reader = csv.DictReader(f)
        return list(reader)   #this line automatically returns list of ordered dictionary

'''a = [1, 2]
b = [3, 4]
c = [5, 6]
write_to_file(a, b, c)'''
write_to_file(movies)
print(read_from_file())