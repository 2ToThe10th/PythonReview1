import string


def encode_caesar(text, key, j):
    return encode_vigenere(text, string.ascii_lowercase[key], j)


def encode_vigenere(text, key, j):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    encoded_text = []

    for i in text:
        if j == len(key):
            j = 0

        if i in lowercase_letters:
            encoded_text.append(
                lowercase_letters[(lowercase_letters.find(i) + lowercase_letters.find(key[j]))
                                  % len(lowercase_letters)])
            j += 1
        elif i in uppercase_letters:
            encoded_text.append(
                uppercase_letters[(uppercase_letters.find(i) + lowercase_letters.find(key[j]))
                                  % len(uppercase_letters)])
            j += 1
        else:
            encoded_text.append(i)

    return tuple([''.join(encoded_text), j])
