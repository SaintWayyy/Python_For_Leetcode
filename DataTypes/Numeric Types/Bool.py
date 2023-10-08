"""
Here are most of the built-in objects considered false:
constants defined to be false: None and False
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '', (), [], {}, set(), range(0)
"""

false_list = [False, None, 0, 0.0, 0j, "", [], (), {}, set(), range(0)]
print(any(false_list))


def _bool():
    # class bool(x=False)
    # Return a Boolean value, i.e. one of True or False.
    # x is converted using the standard truth testing procedure.
    # If x is false or omitted, this returns False; otherwise, it returns True.
    print(bool(0))
    print(bool(1))
    print(bool())


# _bool()
