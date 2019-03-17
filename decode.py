import string

def decode_caesar(text, key):
    return decode_vigenere(text, string.ascii_lowercase[key])


def decode_vigenere(text, key):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    encoded_text = []

    j = 0

    for i in text:
        if j == len(key):
            j = 0

        if i in lowercase_letters:
            encoded_text.append(
                lowercase_letters[(lowercase_letters.find(i) - lowercase_letters.find(key[j]) + len(lowercase_letters))
                                  % len(lowercase_letters)])
        elif i in uppercase_letters:
            encoded_text.append(
                uppercase_letters[(uppercase_letters.find(i) - lowercase_letters.find(key[j]) + len(uppercase_letters))
                                  % len(uppercase_letters)])
        else:
            encoded_text.append(i)

        j += 1

    return ''.join(encoded_text)
