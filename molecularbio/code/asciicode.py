def binary_str(char):
    return (bin(ord(char)))[2:]


def binary_list(text):
    return [ binary_str(x) for x in text ]


def binary(text):
    return "".join(binary_list(text))
