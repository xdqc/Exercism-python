import re
'''
This is not my solution, I borrowed it from @grzegorzme because it was so 
good I thought I should share it.

There are a few things I learned here: re.sub() can take a function as it's second parameter,
sections of a string matched by the regex can be split into groups and accessed, and finally a '\1' 
in a regex indicates that you should only match it to a single char. For example in encode() 
given the string "AAABBCC", the '\1' calls for the regex to match "AAA" "BB" and "CC", otherwise
it would match the whole string (note that \D signifies any non-digit character).
'''

def decode(string):
    return re.sub(r'(\d+)(\D)', lambda m: int(m.group(1)) * m.group(2), string)

def encode(string):
    return re.sub(r'(\D)1+', lambda m: str(len(m.group())) + m.group()[0], string)

