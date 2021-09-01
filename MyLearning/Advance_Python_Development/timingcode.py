import time

def measure_time(func):
    start = time.time()  # time function inside the time module, this returns the number of seconds passed since 1970
    print(start)

    # temp = [x**2 for x in range(5000000)]
    func()

    end = time.time()
    print(end)

    print(end - start)
def powers(limit):
    return [x**2 for x in range(limit)]

measure_time(lambda: powers(5000000)) #here we have to pass it as a lunbda function or else we won't be able to pass the argument

import timeit

print(timeit.timeit("[x**2 for x in range(50)]"))   #timeit returns the average time taken to run a particular statement


