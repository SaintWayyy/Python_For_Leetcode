import math

inf = math.inf
nan = math.nan


def _ceil():
    # math.ceil(x)
    # Return the smallest integer greater than or equal to x.
    # If x is not a float, delegates to x.__ceil__, which should return an Integral value.
    print(math.ceil(1.5))
    print(math.ceil(1))


# _ceil()

def _floor():
    # math.floor(x)
    # Return the largest integer less than or equal to x.
    # If x is not a float, delegates to x.__floor__, which should return an Integral value.
    print(math.floor(1.5))
    print(math.floor(1))


# _floor()


def _trunc():
    # .trunc(x)
    # Return x with the fractional part removed, leaving the integer part.
    # This rounds toward 0: trunc() is equivalent to floor() for positive x,
    # and equivalent to ceil() for negative x.
    # If x is not a float, delegates to x.__trunc__, which should return an Integral value.
    print(math.trunc(1.5))
    print(math.trunc(-1.5))


# _trunc()


def _comb():
    # math.comb(n, k)
    # Return the number of ways to choose k items from n items without repetition and without order.
    print(math.comb(5, 2))


# _comb()


def _perm():
    # math.perm(n, k=None)
    # Return the number of ways to choose k items from n items without repetition and with order.
    print(math.perm(5, 3))


# _perm()


def _copysign():
    # math.copysign(x, y)
    # Return a float with the magnitude (absolute value) of x but the sign of y.
    # On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.
    print(math.copysign(1, -0.0))


# _copysign()


def _fabs():
    # math.fabs(x)
    # Return the absolute value of the float x.
    print(math.fabs(-1))


# _fabs()


def _factorial():
    # math.factorial(n)
    # Return n factorial (n!) as an integer. Raises ValueError if n is not integral or is negative.
    print(math.factorial(5))


# _factorial()


def _fmod():
    # math.fmod(x, y)
    # The intent of the fmod(x, y) is that be exactly (mathematically; to infinite precision)
    # equal to x - n*y for some integer n such that
    # the result has the same sign as x and magnitude less than abs(y).
    # Python’s x % y returns a result with the sign of y instead,
    # and may not be exactly computable for float arguments.
    # fmod() is generally preferred when working with floats,
    # while Python’s x % y is preferred when working with integers.
    print(math.fmod(5, -4))
    print(5 % (-4))

    print(math.fmod(-5, -4))
    print(-5 % (-4))

    print(math.fmod(-5, 4))
    print(-5 % 4)


# _fmod()


def _fsum():
    # math.fsum(iterable)
    # Return an accurate floating point sum of values in the iterable.
    # Avoids loss of precision by tracking multiple intermediate partial sums.
    print(math.fsum([9.99999999, 9.99999999, 9.99999999, 9.99999999, 9.99999999]))


# _fsum()


def _gcd():
    # math.gcd(*integers)
    # Return the greatest common divisor of the specified integer arguments.
    print(math.gcd(-32, 8, 64))


# _gcd()


def _isclose():
    # math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
    # Return True if the values a and b are close to each other and False otherwise.
    print(0.1 + 0.2 == 0.3)
    print(math.isclose(0.1 + 0.2, 0.3))


# _isclose()


def _isfinite():
    # math.isfinite(x)
    # Return True if x is neither an infinity nor a NaN,
    # and False otherwise. (Note that 0.0 is considered finite.)
    print(math.isfinite(nan))
    print(math.isfinite(inf))
    print(math.isfinite(0.0))


# _isfinite()


def _isinf():
    # math.isinf(x)
    # Return True if x is a positive or negative infinity, and False otherwise.
    print(math.isinf(inf))
    print(math.isinf(-99.99))


# _isinf()

def _isnan():
    # math.isnan(x)
    # Return True if x is a NaN (not a number), and False otherwise.
    print(math.isnan(nan))
    print(math.isnan(0.0))


# _isnan()


def _lcm():
    # math.lcm(*integers)
    # Return the least common multiple of the specified integer arguments.
    print(math.lcm(3, 4, 5))


# _lcm()


def _modf():
    # math.modf(x)
    # Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
    print(math.modf(12.123))


# _modf()


def _prod():
    # math.prod(iterable, *, start=1)
    # Calculate the product of all the elements in the input iterable. The default start value for the product is 1.
    # When the iterable is empty, return the start value.
    print(math.prod([10, 11, 12]))


# _prod()


def _log():
    # math.log(x[, base])
    # With one argument, return the natural logarithm of x (to base e).
    # With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).
    print(math.log(8))
    print(math.log(8, 2))


# _log()


def _pow():
    # Return x raised to the power y (always float)
    print(math.pow(10, 2))
    print(math.pow(27, 1 / 3))

# _pow()
