"""
There are three distinct numeric types: integers, floating point numbers, and complex numbers.
In addition, Booleans are a subtype of integers.

When a binary arithmetic operator has operands of different numeric types,
the operand with the “narrower” type is widened to that of the other,
where integer is narrower than floating point, which is narrower than complex.
"""

"""
referred to as integer division. 
For operands of type int, the result has type int. 
For operands of type float, the result has type float. 
In general, the result is a whole integer, though the result’s type is not necessarily int.
"""
print(3 // 2)
print(3.0 // 2)
print(3 // 2.0)
print(3.0 // 2.0)
