def binary_encode(char):
    return (bin(ord(char)))[2:]


def binary_list(text):
    return [ binary_encode(x) for x in text ]


def text_to_binary(text):
    return "".join(binary_list(text))


def char_from_binary(binary):
    num = int(binary, 2)
    return chr(num) if num > 31 and num < 128 else " "


def binary_to_text(chars):
    text = []
    for i in range(0, len(chars), 7):
        text.append(char_from_binary(chars[i:i+7]))
    return "".join(text)
