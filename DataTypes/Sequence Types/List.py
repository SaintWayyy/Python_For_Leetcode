"""
Lists may be constructed in several ways:
Using a pair of square brackets to denote the empty list: []
Using square brackets, separating items with commas: [a], [a, b, c]
Using a list comprehension: [x for x in iterable]
Using the type constructor: list() or list(iterable)
"""

list0 = []
list1 = [3, 1, 2, 4]
list2 = [i for i in range(10, 5, -1)]


def _list():
    # class list
    # class list(iterable)
    # Return a new list object.
    print(list("string"))
    print(list([1, 2, 3, [3, 2, 1]]))


# _list()


def _sort():
    # Sort(*, key=None, reverse=False)
    # This method sorts the list in place, using only < comparisons between items.
    # if any comparison operations fail, the entire sort operation will fail
    # (and the list will likely be left in a partially modified state).
    # key specifies a function of one argument that is used to extract a comparison key from each list element
    # (for example, key=str.lower). The key corresponding to each item in the list is calculated once
    # and then used for the entire sorting process.
    # The default value of None means that list items are sorted directly without calculating a separate key value.
    print(list2)
    list2.sort()
    print(list2)


# _sort()


def n_dimensions_matrix(*args, value=None):
    if len(args) == 0:
        return None

    if any(arg <= 0 for arg in args):
        return None

    def build(*args, value=None):
        if len(args) == 1:
            return [value for _ in range(args[0])]
        else:
            return [build(*args[1:], value=value) for _ in range(args[0])]

    return build(*args, value=value)


# print(n_dimensions_matrix(3, 2, 1, value="se"))
