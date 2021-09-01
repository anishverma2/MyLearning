'''
Generators function remembers the state its in between executions
'''

'''def hundred_numbers():
    num = []
    i = 0
    while i < 100:
        num.append(i)
        i += 1
        
    return num
The above function returns a list of hundred number, and it will return as a list not as each element separately
'''

def hundred_numbers():
    i = 0
    while i < 20:
        yield i     #yield returns the current number which i is currently having whenever we call this function, this is a generator object
        i += 1

print(hundred_numbers()) #this prints that it is a generator object with the memory address not the value of i
g = hundred_numbers()
print(g) #this also prints that g is a generator type object
print(next(g)) #this will print the first value of i
print(next(g))  #this prints the next value of i and similarly we can proceed to the next values
print(list(g))  #list function turns the generator into a list, but starts with where we left off

my_numbers = [x for x in range(5)]  #this is a list comprehension
my_num = (x for x in range(5))  #this is a generator comprehension, this goes over the range one by one and yield the value

print(next(my_num))
print(next(my_num))
print(next(my_num))