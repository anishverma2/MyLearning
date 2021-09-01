import json

my_read = open('csv_file.txt', 'r')
data = [line.strip() for line in my_read.readlines()]
my_read.close()

print(data)

list1 = []
for temp in data:
    club, city, country = temp.split(',')
    list1.append({'club': club, 'city': city, 'country': country})

file = open('json_file.txt', 'w')
json.dump(list1, file)
file.close()
