def _int():
    # class int(x=0)
    # class int(x, base=10)
    # Return an integer object constructed from a number or string x
    # Or return 0 if no arguments are given.
    print(int(1.3))
    print(int("1"))
    print(int())


# _int()


def int_bit_length():
    # int.bit_length()
    # Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:
    int_var = -37
    print(bin(int_var))
    print(int_var.bit_length())


# int_bit_length()


def int_bit_count():
    # Return the number of ones in the binary representation of the absolute value of the integer.
    # This is also known as the population count. Example:
    int_var = -37
    print(bin(int_var))
    print(int_var.bit_count())

# int_bit_count()
