'''
filter is a built in function which takes 2 arguments, first a function which returns true or false
and the 2nd argument has to be an iterable
'''

def starts_with_r(friend):
    return friend.startswith('R')

friends = ['Rolf', 'Fred', 'Sam', 'Randy']
start_with_r = filter(starts_with_r, friends)
'''
we can also use lambda function instead
start_with_r = filter(lambda friend: friend.startswith('R'), friends)
also the above code be written using generator instead of filter
another_starts_with_r = (f for f in friends if f.startswith('R'))  the generator works beter in this case
the interesting thing is filter returns a generator
'''
print(next(start_with_r))
print(next(start_with_r))
print(list(start_with_r))