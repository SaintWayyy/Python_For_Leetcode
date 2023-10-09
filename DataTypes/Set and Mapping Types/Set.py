# class set([iterable])
# class frozenset([iterable])
# Return a new set or frozenset object whose elements are taken from iterable.
# The elements of a set must be hashable. To represent sets of sets, the inner sets must be frozenset objects.
# If iterable is not specified, a new empty set is returned.


# class set
# class set(iterable)
# Return a new set object.

"""
Sets may be constructed in several ways:
Use a comma-separated list of elements within braces: {'jack', 'sjoerd'}
Use a set comprehension: {c for c in 'abracadabra' if c not in 'abc'}
Use the type constructor: set(), set('foobar'), set(['a', 'b', 'foo'])
"""


set0 = set()  # empty set
set1 = {1, 2, 3, 4}  # 使用{}创建set
set2 = {"a", "b", "c", 1, 2, 3, (1, 2, 3)}  # set能包含不同类型的元素




