'''
. - it means letters, numbers, symbols or anything except newlines
+ - it means one or more of
* - it means 0 or more of
? - means 0 or one of

Example:
    .* - means 0 or more of anything, it matched all the character or lines in the world
    .+ - means 1 or more of anything
    [] - matches the character which is present inside the brackets
'''

import re

email = 'anish@gmail.com'
expression = '[a-z]+'   #matches only the character that is anish, gamil and com

matches = re.findall(expression, email)     #turn the matches found into a list

print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'

print(name)
print(domain)

expression1 = '[a-z\.]+'    #now we will have 2 matches anish and gmail.com

matches = re.findall(expression1, email)
print(matches)

name = matches[0]
domain = matches[1]

print(name)
print(domain)

price = 'Price: $189.50'
expression = 'Price: \$([0-9]+\.[0-9]+)'

matches = re.search(expression, price)
print(matches.group(0))     #matches whole thing
print(matches.group(1))     #matches the first thing inside the brackets

'''
.replace function is used to replace any character present in the string with any other character
.replace('c', '') -  replcae all occurance of c with a blank
'''