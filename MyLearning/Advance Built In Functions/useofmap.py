'''
The map function is used to take an iterable and return a new iterable where each iterable has been modified according to some function
'''

friends = ['Rolf', 'Fred', 'Sam', 'Randy']

friends_lower = map(lambda x: x.lower(), friends)
friends_lower_1 = (x.lower for x in friends)    #can also be used as a generator comprehension

print(friends_lower)  #returns that this object is a map object, and we can get the elements using next, as a generator

print(next(friends_lower))
print(next(friends_lower))
