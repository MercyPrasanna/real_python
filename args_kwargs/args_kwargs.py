def add_nos_args(*args):
    """Args takes a variable no of arguments."""
    total = 0
    for no in args:
        total += no
    return total


print(f"The sum of values in the list is {add_nos_args(1,2,3,4,5)}")


def add_nos_kwargs(**kwargs):
    """Kwargs takes a variable no of arguments."""
    total = 0
    for no in kwargs.values():
        total += no
    return total


print(f"The sum of values in the list {add_nos_kwargs(a = 1, b = 3)}")

# Order of the arguments ...
# def my_function(a, b, *args, **kwargs):
#     pass
