def is_isogram(string):
    word = ''.join(filter(str.isalpha, string)).lower()
    return len(set(word))==len(word)
