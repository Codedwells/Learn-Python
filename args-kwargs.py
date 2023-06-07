"""
This is the decorator
"""
def uppercase(func):
    def wrapper():
        function = func()
        uppercased = function.upper()
        return uppercased

    return wrapper


def split_string(func):
    def wrapper():
        function = func()
        splitted = function.split()
        return splitted
    return wrapper

@split_string
@uppercase
def say_Hello():
    return "hello world"


print(say_Hello())
print(uppercase.__doc__)