
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return print("hello world")


say_hi()
