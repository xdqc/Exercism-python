def hey(string):
    if not string.strip():
        return 'Fine. Be that way!'
    elif string.upper() == string and string.lower() != string:
        return 'Whoa, chill out!'
    elif string.rstrip()[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'
