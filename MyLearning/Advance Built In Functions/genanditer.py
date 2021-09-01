class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):     #its a dunder method can be called as next(object), only present in python 3
        if self.number < 100:
            current = self.number
            self.number += 1
            return current  #when we are creating a generator class then we don't require a yield line
        else:
            raise StopIteration()   #to stop the iteration and tells python that we have reached the end of the generator

my_gen = FirstHundredGenerator()
print(my_gen.number)
my_gen.__next__()   #we can call the next method like this also
print(my_gen.number)
next(my_gen)
print(my_gen.number)
print(next(my_gen))    #we can also do this and it gives the previous value not the incremented one
print(my_gen.number)
'''
All objects that are having dunder next method are called iterators
Also not all generators are iterators
Below class is an example of an iterator but its not a generator as it is not generating any number, we are just returning the elements of a list'''

class FirstIteratorNumber:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()

