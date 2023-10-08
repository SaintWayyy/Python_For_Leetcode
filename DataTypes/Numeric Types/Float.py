def _floot():
    # class float(x=0.0)
    # Return a floating point number constructed from a number or string x.
    # Or return 0.0 if no arguments are given.
    print(float(1.334))
    print(float(10))
    print(float())

    # float also accepts the strings “nan” and “inf” with an optional prefix “+” or “-”
    # for Not a Number (NaN) and positive or negative infinity.
    print(float("inf"))
    print(float("+inf"))
    print(float("-inf"))
    print(float("nan"))


def float_as_integer_ratio():
    # Return a pair of integers whose ratio is exactly equal to the original float.
    # The ratio is in lowest terms and has a positive denominator.
    # Raises OverflowError on infinities and a ValueError on NaNs.
    print(float.as_integer_ratio(0.5))


# float_as_integer_ratio()


def float_is_integer():
    # Return True if the float instance is finite with integral value, and False otherwise:
    print((-2.0).is_integer())
    print(2.2.is_integer())


# float_is_integer()
