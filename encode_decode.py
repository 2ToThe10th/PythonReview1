import sys
import encode
import decode
import string


def encode_decode(arguments):
    if arguments['cipher'] in ('caesar', 'vigenere'):
        encode_decode_caesar_vigenere(arguments)
    else:  # arguments['cipher'] == 'vernam'
        encode_decode_vernam(arguments)


def encode_decode_caesar_vigenere(arguments):
    with sys.stdin if arguments['input_file'] is None else open(arguments['input_file'], 'r') as input_file:

        with sys.stdout if arguments['output_file'] is None else open(arguments['output_file'], 'w') as output_file:

            if arguments['cipher'] == 'vigenere':
                key = arguments['key'].lower()

                for i in key:
                    if i not in string.ascii_lowercase:
                        raise ValueError('Bad key')

                encode_fun = encode.encode_vigenere
                decode_fun = decode.decode_vigenere
            else:

                try:
                    key = int(arguments['key'])
                except Exception:
                    raise ValueError('Bad key')

                if key < 0 or key >= len(string.ascii_lowercase):
                    raise ValueError('Bad key')

                encode_fun = encode.encode_caesar
                decode_fun = decode.decode_caesar

            key_index = 0

            if arguments['type'] == 'encode':
                for line in input_file:
                    return_value = encode_fun(line, key, key_index)
                    output_file.write(return_value[0])
                    key_index = return_value[1]
                    output_file.flush()
            else:
                for line in input_file:
                    return_value = decode_fun(line, key, key_index)
                    output_file.write(return_value[0])
                    key_index = return_value[1]
                    output_file.flush()


def encode_decode_vernam(arguments):

    with sys.stdin if arguments['input_file'] is None else open(arguments['input_file'], 'r') as input_file:

        with sys.stdout if arguments['output_file'] is None else open(arguments['output_file'], 'w') as output_file:

            key = arguments['key']
            code_string = string.ascii_uppercase + string.ascii_lowercase + string.digits + ',.'
            code_index = 0
            out_text = []

            for line in input_file:
                for i in line:

                    if i not in code_string:
                        out_text.append(i)
                    else:
                        if code_index >= len(key):
                            raise ValueError('Too small key')
                        out_text.append(code_string[(code_string.find(i) ^ code_string.find(key[code_index]))])
                        code_index += 1

            output_file.write(''.join(out_text))
