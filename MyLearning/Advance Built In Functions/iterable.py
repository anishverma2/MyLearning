'''
Iterable is an object which has iter method in it
once er define __iter__ this method in an object that is now an iterable
'''
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):     #its a dunder method can be called as next(object), only present in python 3
        if self.number < 100:
            current = self.number
            self.number += 1
            return current  #when we are creating a generator class then we don't require a yield line
        else:
            raise StopIteration()

    def __iter__(self):  #now iterator is also a iterable
        return self

'''
All generators are iterators
class FirstHundredIterable:
    def __iter__(self):     #this method tells python that we want to iter over this method, it has to return an iterator
        return FirstHundredGenerator()

print(sum(FirstHundredIterable()))

for i in FirstHundredIterable():
    print(i)
'''
print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)

'''
Another example of iterable without having an iter method in it
'''

class AnotherIterable:
    def __init__(self):
        self.cars = ['Ford', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

for i in AnotherIterable():
    print(i)

'''
Iterator: used to go to the next value using next(iterator)
Iterable: used to go over all the values of iterator
'''