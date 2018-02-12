def is_pangram(string):
    words = ''.join(filter(str.isalpha, string)).lower()
    return len(set(words))==26
