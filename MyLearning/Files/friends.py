friends = input("Enter 3 friends name: ").split()   #friends.split(',')  we can use this to split string on comma or any other symbol we want to give there
set1 = set(friends)

my_read = open("people.txt", 'r')
read_people = [line.strip() for line in my_read.readlines()]   #readlines will read the contents of file line wise and return as a list
print(read_people)  #we have used strip above to remove the \n(newline character) from the list
my_read.close()

set2 = set(read_people)
set3 = set1.intersection(set2)
print(set1, set2, set3)
list2 = list(set3)

my_write = open("nearby_friends.txt", 'w')
for first in list2:
    my_write.writelines(f"{first}\n")   #\n is used to write to new lines

my_write.close()
