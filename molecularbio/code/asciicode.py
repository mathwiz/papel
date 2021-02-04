def binary_string(char):
    return (bin(ord(char)))


def binary_list(text):
    return [ bin(ord(x)) for x in text ]


def binary_string(text):
    return "".join(binary_list(text))
