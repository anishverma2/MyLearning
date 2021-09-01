accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str = 'checking') -> float:  # we can have default value only to the last arguments, we cannot specify default value for first and then no default value
    accounts[name] += amount
    return accounts[name]

add_balance(500.00)

print(accounts['checking'])
