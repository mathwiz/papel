def binary_encode(char):
    return format(ord(char), "07b")


def binary_list(text):
    return [ binary_encode(x) for x in text ]


def text_to_binary(text):
    return "".join(binary_list(text))


def char_from_binary(binary):
    num = int(binary, 2)
    return chr(num) if num > 31 and num < 128 else "?"


def binary_to_text(chars):
    text = []
    for i in range(0, len(chars), 7):
        text.append(char_from_binary(chars[i:i+7]))
    return "".join(text)


def text_with_binary(text):
    chars = [ "   {}   ".format(x) for x in list(text) ]
    codes = binary_list(text)
    return chars, codes


def print_with_decoding(text, width):
    chars, codes = text_with_binary(text)
    printables = list(map(lambda x, y: (x ,y), chars, codes))
    for line1, line2 in printables:
        print(line1)
        print(line2)


def list_of_width(elements, width=80):
    lines = []
    
    return lines

