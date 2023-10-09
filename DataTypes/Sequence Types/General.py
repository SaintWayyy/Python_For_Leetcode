num_list1 = [0, 1, 2, 3, 4, 5]
num_list2 = [-3, -2, -1, 0]


class Num:
    def __init__(self, num=0):
        self.num = num

    def __repr__(self):
        return "Num({})".format(self.num)


"""
Common Sequence Operations
"""


# # s + t: the concatenation of s and t
# print(num_list1 + num_list2)
#
# # Operations
#
# # x in s: True if an item of s is equal to x, else False
# print(1 in num_list1)
# print("gg" in "eggs")
#
# # x not in s: False if an item of s is equal to x, else True
# print(1 not in num_list1)


def _multiply():
    # s * n or n * s: equivalent to adding s to itself n times
    print(num_list1 * 2)

    # Values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as s)
    print(num_list1 * -1)
    print(num_list1 * 0)

    # Items in the sequence s are not copied; they are referenced multiple times.
    matrix = [[Num(3)] * 3] * 3
    print(matrix)

    matrix[0][0].num = 0
    print(matrix)


# _multiply()


def _count():
    # s.count(x): total number of occurrences of x in s
    print(num_list1.count(1))


# _count()


# If i or j is negative, the index is relative to the end of sequence
# s: len(s) + i or len(s) + j is substituted. But note that -0 is still 0.
def _index():
    # s[i]: ith item of s, origin 0
    print(num_list1[0])
    print(num_list1[-1])

    # s.index(x[, i[, j]]):
    # index of the first occurrence of x in s (at or after index i and before index j)
    # raise ValueError when the x is not found.
    print(num_list1.index(1))
    # print(num_list1.index(-1))
    print(num_list1.index(1, -100, 100))


# _index()


def _slicing():
    # s[i:j]: slice of s from i to j
    # s[i:j:k]: slice of s from i to j with step k
    print(num_list1[1:5])
    print(num_list1[1:5:2])
    print()

    # The slice of s from i to j is defined as the sequence of items with index k such that
    # i <= k < j. If i or j is greater than len(s), use len(s).
    print(num_list1[:100])
    print(num_list1[100:])
    print()

    # If i is omitted or None, use 0. If j is omitted or None, use len(s).
    print(num_list1[:])
    print()

    # If i is greater than or equal to j, the slice is empty.
    print(num_list1[2:1])
    print(num_list1[-1:-2])
    print()

    # When k is positive, i and j are reduced to len(s) if they are greater.
    # When k is negative, i and j are reduced to len(s) - 1 if they are greater.
    # If i or j are omitted or None, they become “end” values (which end depends on the sign of k).
    # Note, k cannot be zero. If k is None, it is treated like 1.
    print(num_list1[::-1])
    print(num_list1[100:-100:-1])
    print()

    # Slicing creates a shallow copy
    num_list = [Num(0), Num(1), Num(2)]
    num_list_slice = num_list[:]
    num_list_slice[0] = "hello"
    print(num_list)
    print(num_list_slice)

    num_list_slice[2].num = 99
    print(num_list)
    print(num_list_slice)


# _slicing()


"""
Mutable Sequence Types Operations
"""


# # s[i] = x: item i of s is replaced by x
# num_list1[0] = 50
# print(num_list1)
#
# # s[i:j] = t: slice of s from i to j is replaced by the contents of the iterable t
# num_list1[:1] = [6, 5, 4]
# print(num_list1)
#
# # del s[i:j]: same as s[i:j] = []
# del num_list1[:3]
# print(num_list1)
#
# # s[i:j:k] = t: The elements of s[i:j:k] are replaced by those of t
# # t must have the same length as the slice it is replacing.
# num_list1[0:4:2] = ["a", "b"]
# print(num_list1)
#
# # del s[i:j:k]: removes the elements of s[i:j:k] from the list
# del num_list1[0:4:2]
# print(num_list1)
#

#
# # s *= n: updates s with its contents repeated n times
# # Items in the sequence are not copied; they are referenced multiple times, as explained for s * n
# num_list1 *= 2
# print(num_list1)


def _append():
    # s.append(x): appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
    num_list1.append(6)
    num_list1[len(num_list1):] = [7]
    num_list1.append(["3", "2", "1"])
    print(num_list1)


# _append()


def _clear():
    # s.clear(): removes all items from s (same as del s[:])
    num_list1.clear()
    print(num_list1)


# _clear()


def _extend():
    # s.extend(t) or s += t: extends s with the contents of t
    # (for the most part the same as s[len(s):len(s)] = t)
    global num_list1
    num_list1.extend([1, 2, 3, 4, 5])
    num_list1 += [1, 2, 3]
    print(num_list1)


# _extend()


def _insert():
    # s.insert(i, x): inserts x into s at the index given by i (same as s[i:i] = [x])
    num_list1.insert(0, 0)
    print(num_list1)


# _insert()


def _pop():
    # s.pop() or s.pop(i): retrieves the item at i and also removes it from s
    num_list1.pop(len(num_list1) - 1)
    print(num_list1)


# _pop()


def _remove():
    # s.remove(x): remove the first item from s where s[i] is equal to x
    num_list1.remove(0)
    print(num_list1)


# _remove()


def _reverse():
    # s.reverse(): reverses the items of s in place
    num_list1.reverse()
    print(num_list1)

# _reverse()
