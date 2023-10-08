def positional_args(arg1: int, arg2: int) -> None:
    pass
    print("arg1 =", arg1, "arg2 =", arg2)
    return  # 可选，用于返回值


# Positional Arguments:
# They are passed to a function in the order in which they are defined in the function's parameter list.
positional_args(1, 2)

# Keyword Arguments:
# They are passed to a function by providing its name and value, the oder is not matter.
positional_args(arg2=2, arg1=1)
print()

"""
# keyword arguments must follow positional arguments
positional_args(arg1=1, 2)
# SyntaxError: positional argument follows keyword argument
"""


# Default Arguments: arguments that have default values，
def default_args(arg=0):
    print(arg)
    return


default_args()  # Default Arguments Are Optional
default_args(10)
print()

"""
# Default arguments must follow non-default arguments
def default_args(arg1=0, arg2):
    pass
# SyntaxError: non-default argument follows default argument
"""


# Variable-Length Arguments
def variable_length_positional_args(*args, **kwargs):
    print(type(args))
    for p in args:
        print(p, end=" ")
    print()

    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
    print()
    return


variable_length_positional_args(5, 4, 3, first=1, second=2, last=3)
print()


# all the parameters before the / must be positional-only parameters,
# all the parameters after the * must be keyword-only arguments,
def slash_and_asterisk(pos, /, pos_or_kwd, *, kwd):
    print(pos, pos_or_kwd, kwd)
    return


slash_and_asterisk(1, 2, kwd=3)


# Lambda functions
def multiply(n):
    return lambda a: a * n


double = multiply(2)
print(double(10))
print()


