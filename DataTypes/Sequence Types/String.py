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
# print("spam " "eggs" == "spam eggs")

# A backslash can be added at the end of a line to ignore the newline:
s3 = 'This string will not include \
backslashes or newline characters.'


# print(s3)


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


def str_count():
    # str.count(sub[, start[, end]]) Return the number of non-overlapping occurrences of substring sub in the range [
    # start, end]. Optional arguments start and end are interpreted as in slice notation. If sub is empty,
    # returns the number of empty strings between characters which is the length of the string plus one.
    print("aaaa".count("aa"))


# str_count()


def str_find():
    # str.find(sub[, start[, end]])
    # Return the lowest index in the string where substring sub is found within the slice s[start:end].
    # Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
    print("aa aa aa".find("aa"))


# str_find()


def str_rfind():
    # str.rfind(sub[, start[, end]])
    # Return the highest index in the string where substring sub is found,
    # such that sub is contained within s[start:end].
    # Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
    print("aa aa aa".rfind("aa"))


# str_rfind()


def str_format():
    # format(value, format_spec='')
    # Convert a value to a “formatted” representation, as controlled by format_spec.
    print('{}, {}, {}'.format('a', 'b', 'c'))
    print('{2}, {1}, {0}'.format('a', 'b', 'c'))
    print('{0} {1} {0}'.format('a', 'b'))

    # The * operator for sequence unpacking
    print(*"abc")
    print('{2}, {1}, {0}'.format(*'abcdefg'))

    hello = "hello"
    world = "world"
    print(f"{hello} {world}")


# str_format()


def str_islower():
    # str.islower()
    # Return True if all cased characters in the string are lowercase
    # and there is at least one cased character, False otherwise.
    print("abc".islower())
    print("Abc".islower())


# str_islower()


def str_isupper():
    # str.isupper()
    # Return True if all cased characters in the string are uppercase
    # and there is at least one cased character, False otherwise.
    print("ABC".isupper())
    print("AbC".isupper())


# str_isupper()


def str_join():
    # str.join(iterable)
    # Return a string which is the concatenation of the strings in iterable.
    # The separator between elements is the string providing this method.
    print(":".join(["a", 'b', 'c']))


# str_join()


def str_lower():
    # str.lower()
    # Return a copy of the string with all the cased characters converted to lowercase.
    print("ABC".lower())


# str_lower()


def str_upper():
    # str.upper()
    # Return a copy of the string with all the cased characters converted to uppercase.
    print("abc".upper())


# str_upper()


def str_strip():
    # str.strip([chars])
    # Return a copy of the string with the leading and trailing characters removed.
    # The chars argument is a string specifying the set of characters to be removed.
    # If omitted or None, the chars argument defaults to removing whitespace.
    # The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:
    print("     abc       ".strip())


# str_strip()


def str_lstrip():
    # str.lstrip([chars])
    # Return a copy of the string with leading characters removed.
    # The chars argument is a string specifying the set of characters to be removed.
    # If omitted or None, the chars argument defaults to removing whitespace.
    # The chars argument is not a prefix; rather, all combinations of its values are stripped.
    print("abcabc-abcabc".lstrip("abc"))


# str_lstrip()


def str_rstrip():
    # str.rstrip([chars])
    # Return a copy of the string with trailing characters removed.
    # The chars argument is a string specifying the set of characters to be removed.
    # If omitted or None, the chars argument defaults to removing whitespace.
    # The chars argument is not a suffix; rather, all combinations of its values are stripped.
    print("abcabc-abcabc".rstrip("abc"))


# str_rstrip()


def str_replace():
    # str.replace(old, new[, count])
    # Return a copy of the string with all occurrences of substring old replaced by new.
    # If the optional argument count is given, only the first count occurrences are replaced.
    print("hello world".replace("hello", "hi"))


# str_replace()


def str_split():
    # str.split(sep=None, maxsplit=-1)
    # Return a list of the words in the string, using sep as the delimiter string.
    # If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements).
    # If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
    print(",".split(","))
    print("1,2,3".split(","))
    print(",1,,2,3,".split(","))
    print("aaa".split("a"))


str_split()


def str_rsplit():
    # str.rsplit(sep=None, maxsplit=-1)
    # Return a list of the words in the string, using sep as the delimiter string.
    # If maxsplit is given, at most maxsplit splits are done, the rightmost ones.
    # If sep is not specified or None, any whitespace string is a separator.
    # Except for splitting from the right, rsplit() behaves like split().
    print(",".rstrip(","))
    print("1,2,3".rsplit(","))
    print(",1,,2,3,".rsplit(","))
    print("aaa".rsplit("a"))


# str_rsplit()
