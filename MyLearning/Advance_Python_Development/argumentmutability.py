friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

def see_friends(friends, name):
    print(id(friends))
    friends[name] = 0

print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))
print(friends_last_seen['Rolf'])
see_friends(friends_last_seen, 'Rolf') #here the value gets passed as a reference, th address gets passed not the value, so once we changed the value in the function it get reflected outside the function also
print(id(friends_last_seen['Rolf']))
print(friends_last_seen['Rolf'])
print(id(friends_last_seen))


age = 20

def increase_age(current_age):
    print(id(current_age))  #here also the argument is passed as a reference but since integers are immutable, another object get returned by the below line so the value didn't get reflected outside the function
    current_age = current_age + 1  #here a new object gets returned so the id also gets modified
    print(id(current_age))

print(id(age))
increase_age(age)
print(id(age))
print(age)

primes = [3, 5, 7]
print(id(primes))

primes += [11, 13] #primes.__iadd__() this method gets called here
print(id(primes))
print(primes)

primes = primes + [17]  #primes.__add__() this method gets called here and this is totally different case and in this case a new object gets returned and id changes
print(id(primes))