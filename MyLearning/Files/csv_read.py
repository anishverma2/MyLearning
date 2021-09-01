my_read = open('csv_data.txt', 'r')
data = [line.strip() for line in my_read.readlines()]
my_read.close()

data = [line.split(',') for line in data[1:]]
print(data)

for d1 in data:
    name = d1[0].title()
    age = d1[1]
    degree = d1[2].capitalize()
    university = d1[3].upper()
    print(f"{name} is {age}, studying {degree} from {university}")

    sample_csv_join = ','.join(d1) #join is used to join the elements of a list using comma as a seperator
    print(sample_csv_join)