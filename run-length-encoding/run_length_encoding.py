def decode():
    pass


def encode(str):
    current = str.startswith()
    num = 1
    output = ''
    for char in str:
        if char == current:
            num += 1
        else:
            output += char

