'''
any func takes an iterable and returns true if any of its value is true
and all function returns true if all the values evaluates to true
Below things evaluates to False
0, 0.0
[],{}, ()
None
False
'''

friends = [
  {
    'name': 'Rolf',
    'location': 'Washington, D.C.'
  },
  {
    'name': 'Anna',
    'location': 'San Francisco'
  },
  {
    'name': 'Charlie',
    'location': 'San Francisco'
  },
  {
    'name': 'Jose',
    'location': 'San Francisco'
  },
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
  print('You are not alone!')