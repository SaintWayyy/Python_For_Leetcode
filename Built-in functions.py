import random

positive_int = 1
negative_int = -1
positive_float = 1.0
negative_float = -1.0

bool_list = [True, True, True]
num_list = [3, 1, 0, -1, -3, -5]


def _abs():
    # abs(x):
    # Return the absolute value of a number.
    print(abs(negative_int))
    print(abs(negative_float))


# _abs()


def _all():
    # all(iterable):
    # Return True if all elements of the iterable are true (or if the iterable is empty).
    print(all(bool_list))


# _all()


def _any():
    # any(iterable):
    # Return True if any element of the iterable is true. If the iterable is empty, return False.
    print(any(bool_list))


# _any()


def _bin():
    # bin(x):
    # Convert an integer number to a binary string prefixed with “0b”.
    print(bin(positive_int))
    print(bin(negative_int))


# _bin()


def _oct():
    # oct(x)
    # Convert an integer number to an octal string prefixed with “0o”.
    print(oct(positive_int))
    print(oct(negative_int))


# _oct()


def _hex():
    # hex(x):
    # Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.
    print(hex(positive_int))
    print(hex(negative_int))


# _hex()


def _divmod():
    # divmod(a, b)
    # Take two (non-complex) numbers as arguments and return a pair of numbers
    # consisting of their quotient and remainder when using integer division.
    # With mixed operand types, the rules for binary arithmetic operators apply.
    print(divmod(11, 3))
    print(divmod(11.0, 3.0))


# _divmod()


def _enumerate():
    # enumerate(iterable, start=0):
    # Return an enumerate object.
    """
    same as:
    def enumerate(iterable, start=0):
        n = start
        for elem in iterable:
            yield n, elem
            n += 1
    """
    print(list(enumerate(bool_list)))


# _enumerate()


def _eval():
    # eval(expression, globals=None, locals=None):
    # expression argument is parsed and evaluated as a Python expression
    print(eval("positive_int + negative_int + positive_float + negative_float"))


# _eval()

def _filter():
    # filter(function, iterable)
    # Construct an iterator from those elements of iterable for which function is true.
    # If function is None, the identity function is assumed, that is,
    # all elements of iterable that are false are removed.
    print(list(filter(lambda x: x > 0, num_list)))
    print(list(filter(None, num_list)))


# _filter()


def _frozenset():
    # class frozenset(iterable=set()):
    # Return a new frozenset object, optionally with elements taken from iterable.
    print(frozenset(bool_list))


# _frozenset()

def _iter():
    # iter(object)
    # iter(object, sentinel)
    # Return an iterator object.
    for i in iter(num_list):
        print(i, end=" ")

    for i in iter(lambda: random.randint(0, 5), 3):
        print(i, end=" ")
    return


# _iter()


def _next():
    # next(iterator)
    # next(iterator, default)
    # Retrieve the next item from the iterator by calling its __next__() method.
    # If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.
    print(next(iter(num_list)))


# _next()


def _len():
    # len(s):
    # Return the length (the number of items) of an object.
    # The argument may be a sequence (such as a string, bytes, tuple, list, or range)
    # or a collection (such as a dictionary, set, or frozen set).
    print(len(bool_list))


# _len()


def _map():
    # map(function, iterable, *iterables)
    # Return an iterator that applies function to every item of iterable, yielding the results.
    # If additional iterables arguments are passed,
    # function must take that many arguments and is applied to the items from all iterables in parallel.
    # With multiple iterables, the iterator stops when the shortest iterable is exhausted.

    it = map(lambda x: print(x, end=" "), num_list)
    for _ in it:
        pass
    print()


# _map()


def _max():
    # max(iterable, *, key=None)
    # max(iterable, *, default, key=None)
    # max(arg1, arg2, *args, key=None)
    # Return the largest item in an iterable or the largest of two or more arguments.
    # The key argument specifies a one-argument ordering function like that used for list.sort().
    # The default argument specifies an object to return if the provided iterable is empty.
    print(max(num_list))
    print(max([], default=0))
    print(max(num_list, key=abs))


# _max()


def _min():
    # min(iterable, *, key=None)
    # min(iterable, *, default, key=None)
    # min(arg1, arg2, *args, key=None)
    # Return the smallest item in an iterable or the smallest of two or more arguments.
    print(min(num_list))
    print(min([], default=0))
    print(min(num_list, key=abs))


# _min()


def _pow():
    # pow(base, exp, mod=None)
    # Return base to the power exp; if mod is present, return base to the power exp,
    # modulo mod (computed more efficiently than pow(base, exp) % mod).
    # The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.
    print(pow(10, 2))
    print(pow(10, 2.0))
    print(pow(10.0, 2))
    print(pow(10, 2, 5))


# _pow()


def _print():
    # print(*objects, sep=' ', end='\n', file=None, flush=False)
    # Print objects to the text stream file, separated by sep and followed by end.
    print(1, 2, 3, sep="-", end="END")


# _print()


def _round():
    # round(number, ndigits=None)
    # Return number rounded to ndigits precision after the decimal point.
    # If ndigits is omitted or is None, it returns the nearest integer to its input.
    print(round(1.11111, 2))
    print(round(1.5))


# _round()


def _slice():
    # class slice(stop)
    # class slice(start, stop, step=None)
    # Return a slice object representing the set of indices specified by range(start, stop, step).
    # Slice objects are also generated when extended indexing syntax is used.
    # For example: a[start:stop:step] or a[start:stop, i]
    end = len(num_list)
    print(num_list[slice(0, end, 2)])


# _slice()


def _sorted():
    # sorted(iterable, /, *, key=None, reverse=False)
    # Return a new sorted list from the items in iterable.
    # key specifies a function of one argument that is used to
    # extract a comparison key from each element in iterable (for example, key=str.lower).
    # The built-in sorted() function is guaranteed to be stable.
    print(num_list)
    print(sorted(num_list))
    print(num_list)
    print(sorted("124144513"))


# _sorted()

def _sum():
    # sum(iterable, /, start=0)
    # Sums start and the items of an iterable from left to right and returns the total.
    # The iterable’s items are normally numbers, and the start value is not allowed to be a string.
    print(sum(num_list))


# _sum()


def _type():
    # class type(object)
    # class type(name, bases, dict, **kwds)
    # With one argument, return the type of an object.
    print(type(1))
    print(type(True))
    print(type([]))


# _type()


def _zip():
    # zip(*iterables, strict=False)
    # zip() returns an iterator of tuples,
    # where the i-th tuple contains the i-th element from each of the argument iterables.
    # zip() is lazy: The elements won’t be processed until the iterable is iterated on

    # By default, zip() stops when the shortest iterable is exhausted.
    # It will ignore the remaining items in the longer iterables,
    # cutting off the result to the length of the shortest iterable:
    # if strict=True, it raises a ValueError if one iterable is exhausted before the others
    for item in zip(bool_list, num_list):
        print(item)

    for item in zip(num_list):
        print(item)

    # zip() in conjunction with the * operator can be used to unzip a list:
    x = [1, 2, 3]
    y = [4, 5, 6]

    x2, y2 = zip(*zip(x, y))
    print(x == list(x2) and y == list(y2))

# _zip()
