'''
counter
defaultdict
ordereddict
namedtuple
deque
'''

from collections import Counter

device_temperature = [13.5, 14.0, 14.5, 14.5, 14.0, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperature)
print(temperature_counter[14.5])

print(Counter({'Hello': 3, 'Hi': 2})['Hi'])

from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_matters = {}

for coworker, place in coworkers:
    if coworker not in alma_matters:
        alma_matters[coworker] = []
    alma_matters[coworker].append(place)

print(alma_matters)

#Another Approach
alma_matters1 = defaultdict(list)

for coworker, place in coworkers:
    alma_matters1[coworker].append(place)

alma_matters1.default_factory = None  #to raise an Error when we try to access a key which doesn not exist

print(alma_matters1['Rolf'])

#Another Approach
my_company = 'Telecado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_company = defaultdict(lambda: my_company) #this provide a default value to the key which is not present in the dictionary

for person, company in other_coworkers:
    coworker_company[person] = company

print(coworker_company[coworkers[0]])
print(coworker_company['Rolf'])
for i in coworker_company:
    print(i)
#print(coworker_company)

from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jen'] = 12
o['Jose'] = 18

print(o)    #OrderedDict means that the keys will be displayed in the order in which it is inserted into the dictionary
#However it is not that useful bcoz Python 3.7 and above already retain the dictionary orer in which the elements are inserted

o.move_to_end('Rolf')   #this moves the key 'Rolf' to the end
o.move_to_end('Jose', last=False)   #this moves Jose to the start

print(o)

o.popitem()     #in this the last item will get popped off

print(o)

from collections import namedtuple

account = ('checking', 1850.00)

Account = namedtuple('Account', ['name', 'balance']) #giving name to the values of the tuples

account = Account('checking', 1850.00)  #now checking is linked to name and 1850.00 linked to balance

print(account.name)
print(account)  #shows name and value pair: Account(name='checking', balance=1850.0)

from collections import deque
#deque is double ended queue

friends = deque(('Rolf', 'Jen', 'Jose'))

friends.append('Joi')   #add an element to the end
friends.appendleft('Matt')  #add an element to the start

print(friends)

friends.pop()   #delete an element from the end
temp = friends.popleft()   #delete an element from the start

print(friends, temp)
