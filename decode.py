import string

def decode_ces_vig(text, key):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    uppercase_key = key.upper()

    decoded_text = []

    for i in text:
        if i in key:
            decoded_text.append(lowercase_letters[key.find(i)])
        elif i in uppercase_key:
            decoded_text.append(uppercase_letters[uppercase_key.find(i)])
        else:
            decoded_text.append(i)

    return ''.join(decoded_text)
