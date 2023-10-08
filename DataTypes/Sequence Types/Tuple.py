"""
Tuple may be constructed in several ways:
Using a pair of parentheses to denote the empty tuple: ()
Using a trailing comma for a singleton tuple: a, or (a,)
Separating items with commas: a, b, c or (a, b, c)
Using the tuple() built-in: tuple() or tuple(iterable)
"""

tuple0 = ()  # empty tuple
tuple1 = (1,)
tuple3 = (1, 2, 3)


def _tuple():
    # class tuple
    # class tuple(iterable)
    # Return a new tuple object.
    print(tuple(x for x in range(5, 10)))


_tuple()

