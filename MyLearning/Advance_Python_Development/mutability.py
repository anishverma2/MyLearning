'''
Mutable: the piece of data which we can change after we created it
Immutable: piece of data which we cannot change once created
'''

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen)) #id returns the first cell or first address of the allocated memory
#both the times new dictionaries are created so their id are different
friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}
print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0
print(id(friends_last_seen)) #last id and this id are same so dictionaries are mutable

my_int = 5
print(id(my_int))
my_int = my_int + 1     #or we can try my_int = 6 or my_int += 1, all 3 cases new object is returned so id changes
print(id(my_int))   #integers are immutable, we cannot modify the value, it get stored at a new place

'''
other immutable things are: 
int  -> all functions returns new objects
float, strings and tuples
'''

#however lists are mutable

friends = ['R', 'J']
print(id(friends))

friends.append('Z')
print(id(friends))