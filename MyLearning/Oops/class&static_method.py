class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
print(my_object.hi())   #here the class is passed as an argument


class Bar:
    @staticmethod
    def hi():
        print("Hey, I don't take any parameters")

another_object = Bar()
another_object.hi()     #this method doesn't take any parameters


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)


number = FixedFloat(18.576)
print(number)

new_num = FixedFloat.from_sum(12.12, 14.14)
print(new_num)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

    # Skip defining from_sum as that's inherited

"""
We’ve defined this new class that extends the `FixedFloat ` class. It’s got an `__init__` method that calls the parent’s `__init__`, and a `__repr__` method that overrides the parents’. It doesn’t have a `from_sum` method as that’s inherited and we’ll just use the one the parent defined.
"""

euros = Euro(18.5963)
print(euros)  # <Euro €18.59>

result = Euro.from_sum(15.76, 19.905)
print(result)  # <FixedFloat 35.66>

"""
Oops! When we called the `Euro` constructor directly, we got a `Euro ` object with the symbol. But when we call `from_sum`, we got a `FixedFloat ` object. Not what we wanted!

In order to fix this, we must make the `from_sum` method return an object of the class that called it—so that:

* `FixedFloat.from_sum()` returns a `FixedFloat ` object; and
* `Euro.from_sum()` returns an `Euro` object.

`@classmethod` to the rescue! If we modify the `FixedFloat` class:
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)
"""