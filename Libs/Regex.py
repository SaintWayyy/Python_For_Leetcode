import re

pattern = re.compile('[a-z]+')
match1 = pattern.match("123")
match2 = pattern.match("abc")

# Return the string matched by the regex
match2.group()

# Return the starting position of the match
match2.start()

# Return the ending position of the match
match2.end()

# Return a tuple containing the (start, end) positions of the match
match2.span()