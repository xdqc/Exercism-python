def decode(input):
    out, num = '', ''
    for char in input:
        if char.isnumeric():
            num += char
        else:
            out += char * (1 if num=='' else int(num))
            num = ''
    return out



def encode(input):
    input+='0'      #append a placeholder to the end of string
    out, num, prev = '', 0, input[0]
    for char in input:
        if prev == char:
            num += 1
        else:
            out += ('' if num==1 else str(num)) + prev
            num, prev = 1, char
    return out

