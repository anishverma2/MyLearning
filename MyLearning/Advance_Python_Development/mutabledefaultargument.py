#its a bad idea, we should not do it
''''
we can also use the below approach
def create_account(name: str, holder: str, account_holders = None):
    if account_holders is None:
        account_hilders = []
'''
def create_account(name: str, holder: str, account_holders: list = []):
    print(id(account_holders))
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')

print(a1)
print(a2)
'''
here the list account_holders gets created when the function is defined, not at the time of calling, 
so whenever we call this all those values gets appended to the list and get returned to the calling variable
'''

# to solve this problem whenever we call the function we should pass an empty list so that it should not take the default one as argument

a3 = create_account('checking', 'Sam', [])
print(a3)