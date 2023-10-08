# class range(stop)
# class range(start=0, stop[, step=1])

# For a positive step, the contents of a range r are determined by the formula
# r[i] = start + step*i where i >= 0 and r[i] < stop.
print(list(range(10)))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))

# For a negative step, the contents of the range are still determined by the formula
# r[i] = start + step*i, but the constraints are i >= 0 and r[i] > stop.
print(list(range(0, -10, -1)))

# A range object will be empty if r[0] does not meet the value constraint.
print(list(range(10, -10, 1)))
print(list(range(0)))

# Range objects implement the collections.abc.Sequence ABC,
# and provide features such as containment tests,
# element index lookup, slicing and support for negative indices
r = range(0, 20, 2)
print(13 in r)
print(10 in r)
print(r.index(10))
print(list(r[:5]))
print(r[-1])

# Two range objects are considered equal if they represent the same sequence of values
print(range(0, 3, 2) == range(0, 4, 2))
