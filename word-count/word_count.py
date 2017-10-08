import re

def word_count(words):
    words = re.findall(r'[^\W_]+', words.lower())
    count = dict()
    for word in words:
        count[word] = count.setdefault(word,0)+1
    return count
