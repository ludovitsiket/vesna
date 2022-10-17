#!/usr/bin/python3
import sys


def decompose(value):
    text = []
    for char in value:
        text.append(char)
    return text


def translation(decomp, alphabet):
    num = []
    for item in range(len(decomp)):
        try:
            number_value = alphabet.index(decomp[item])
            num.append(number_value + 1)
        except ValueError as e:
            print(e)
            sys.exit()
    return num


def abc():
    # slovak alphabet
    small_letters = [
        "a",
        "á",
        "ä",
        "b",
        "c",
        "č",
        "d",
        "ď",
        "dž",
        "e",
        "é",
        "f",
        "g",
        "h",
        "i",
        "í",
        "j",
        "k",
        "l",
        "ĺ",
        "ľ",
        "m",
        "n",
        "ň",
        "o",
        "ó",
        "ô",
        "p",
        "q",
        "r",
        "ŕ",
        "s",
        "š",
        "t",
        "ť",
        "u",
        "ú",
        "v",
        "w",
        "x",
        "y",
        "ý",
        "z",
        "ž"]

    chars = [
        ",",
        ".",
        "!",
        "?",
        "_",
        "-",
        ";",
        "/",
        "=",
        "*",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        " ",
        "+",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9"]

    big_letters = [
        "A",
        "Á",
        "B",
        "C",
        "Č",
        "D",
        "Ď",
        "DŽ",
        "E",
        "É",
        "F",
        "G",
        "H",
        "I",
        "Í",
        "J",
        "K",
        "L",
        "Ĺ",
        "Ľ",
        "M",
        "N",
        "Ň",
        "O",
        "Ó",
        "P",
        "Q",
        "R",
        "Ŕ",
        "S",
        "Š",
        "T",
        "Ť",
        "U",
        "Ú",
        "V",
        "W",
        "X",
        "Y",
        "Ý",
        "Z",
        "Ž"]
    return (small_letters + chars + big_letters)


def make_keys(alphabet):
    x = 1
    y = []
    while x < (len(alphabet) + 1):
        y.append(x)
        x += 1
    return y


def make_dict(alphabet, keys):
    x = 0
    dictionary = dict.fromkeys(keys)
    while x < (len(alphabet)):
        dictionary[x] = alphabet[x - 1]
        x += 1
    return dictionary


def multi_replace(content, to_replace, repl):
    for elem in to_replace:
        if elem in content:
            content = content.replace(elem, repl)
    return content


def read_file(some_file):
    with open(some_file, 'r') as msg:
        con = msg.read()
        con = multi_replace(con, ['\n', '[', ']'], "")
    return con


def write_file(file_to_write, con):
    with open(file_to_write, 'w') as msg:
        msg.write(str(con))
    return msg


def help_syntax():
    print("Skcipt require python3.x")
    print("""Syntax: python3 vesna.py parameters
Message for coding must be in file sprava.txt,
for decoding must be coded message in file kodovana.txt
Parameters: 'k' for coding file
           'd' for decoding file""")


def coding(message_file, alphabet, coded_message):
    msg = read_file(message_file)
    decomp = decompose(msg)
    num = translation(decomp, alphabet)
    write_file(coded_message, num)
    print("OK")


def slicing_list(content):
    result = []
    a = 0
    b = 3
    character = ','
    length = range(len(content) + b)
    while b in length:
        decoded = (content[a:b])
        if character in decoded:
            decoded = decoded.replace(character, '')
        result.append(decoded)
        a += 3
        b += 3
    return result


def processing_decode(coded_message):
    content = []
    con = read_file(coded_message)
    for item in con:
        item = multi_replace(item, [' ', '[', ']'], "")
        content.append(item)
    content = ''.join(content)
    return content


def decoding(coded_message, dictionary):
    content = processing_decode(coded_message)
    number_result = slicing_list(content)
    index = 0
    while index < len(number_result):
        for _ in number_result:
            key = str(number_result[index])
            print(dictionary[int(key)], end='')
            index += 1
    print('')


def exception(e):
    print(e)
    help_syntax()
    sys.exit()


def processing():
    try:
        arg = sys.argv[1]
    except IndexError as e:
        arg = False
        exception(e)
    except SyntaxError as e:
        print(e)
        sys.exit()
    alphabet = abc()
    keys = make_keys(alphabet)
    dictionary = make_dict(alphabet, keys)
    message_file = "sprava.txt"
    coded_message = "kodovana.txt"
    try:
        if arg == 'k':
            coding(message_file, alphabet, coded_message)
        elif arg == 'd':
            decoding(coded_message, dictionary)
        else:
            help_syntax()
            sys.exit()
    except FileNotFoundError as e:
        exception(e)


if __name__ == '__main__':
    try:
        processing()
    except KeyboardInterrupt:
        sys.exit()
