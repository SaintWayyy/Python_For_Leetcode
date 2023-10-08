"""
String literals are written in a variety of ways:
Single quotes: 'allows embedded "double" quotes'
Double quotes: "allows embedded 'single' quotes"
Triple quoted: '''Three single quotes''', \"""Three double quotes\"""
"""

s1 = "string1"
s2 = "string2"

# String literals that are part of a single expression and have only whitespace between them
# will be implicitly converted to a single string literal. That is, ("spam " "eggs") == "spam eggs".
print("spam " "eggs" == "spam eggs")

# A backslash can be added at the end of a line to ignore the newline:

s3 = 'This string will not include \
backslashes or newline characters.'
print(s3)


def _str():
    # class str(object='')
    # class str(object=b'', encoding='utf-8', errors='strict')
    # Return a str version of object.
    print(str(999))
    print(str(1.2))
    print(str(True))


# _str()


def _chr():
    # chr(i): Return the string representing a character whose Unicode code point is the integer i.
    print(chr(97))


# _chr()


def _ord():
    # ord(c)
    # Given a string representing one Unicode character,
    # return an integer representing the Unicode code point of that character.
    print(ord('a'))


# _ord()


def _format():
    # format(value, format_spec='')
    # Convert a value to a “formatted” representation, as controlled by format_spec.
    print('{}, {}, {}'.format('a', 'b', 'c'))
    print('{2}, {1}, {0}'.format('a', 'b', 'c'))
    print('{0} {1} {0}'.format('a', 'b'))

    # The * operator for sequence unpacking
    print(*"abc")
    print('{2}, {1}, {0}'.format(*'abc'))


_format()
