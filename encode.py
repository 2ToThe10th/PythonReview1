import string

def encode_ces_vig(text, key):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    uppercase_key = key.upper()

    encoded_text = []

    for i in text:
        if i in lowercase_letters:
            encoded_text.append(key[lowercase_letters.find(i)])
        elif i in uppercase_letters:
            encoded_text.append(uppercase_key[uppercase_letters.find(i)])
        else:
            encoded_text.append(i)

    return ''.join(encoded_text)
