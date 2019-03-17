import sys
import parser
import encode
import decode
import string

arguments = parser.parse()

if arguments['type'] in ('encode', 'decode') and arguments['cipher'] in ('caesar', 'vigenere'):
    if arguments['input_file'] is None:
        input_file = sys.stdin
        print('Input from stdin.\nTo exit programme type "exit"')
    else:
        try:
            input_file = open(arguments['input_file'], 'r')
        except:
            raise ValueError('Problems with input_file')

    if arguments['output_file'] is None:
        output_file = sys.stdout
    else:
        try:
            output_file = open(arguments['output_file'], 'w')
        except:
            raise ValueError('Problems with output_file')

    if arguments['cipher'] == 'vigenere':
        key = arguments['key'].lower()

        for i in key:
            if i not in string.ascii_lowercase:
                raise ValueError('Bad key');

        encode_fun = encode.encode_vigenere
        decode_fun = decode.decode_vigenere
    else:

        try:
            key = int(arguments['key'])
        except:
            raise ValueError('Bad key')

        if key < 0 or key >= len(string.ascii_lowercase):
            raise ValueError('Bad key')

        encode_fun = encode.encode_caesar
        decode_fun = decode.decode_caesar

    if arguments['type'] == 'encode':
        for line in input_file:
            if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                break
            output_file.write(encode_fun(line, key))
            output_file.flush()
    else:
        for line in input_file:
            if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                break
            output_file.write(decode_fun(line, key))
            output_file.flush()

    input_file.close()
    output_file.close()

if arguments['type'] in ('encode', 'decode') and arguments['cipher'] == 'vernam':

    if arguments['input_file'] is None:
        input_file = sys.stdin
        print('Input from stdin.\nTo exit programme type "exit"')
    else:
        try:
            input_file = open(arguments['input_file'], 'r')
        except:
            raise ValueError('Problems with input_file')

    if arguments['output_file'] is None:
        output_file = sys.stdout
    else:
        try:
            output_file = open(arguments['output_file'], 'w')
        except:
            raise ValueError('Problems with output_file')

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
    input_file.close()
    output_file.close()


if arguments['type'] == 'train':
    print(arguments)

    if arguments['text_file'] is None:
        text_file = sys.stdin
        print('Input from stdin.\nTo exit programme type "exit"')
    else:
        try:
            text_file = open(arguments['text_file'], 'r')
        except:
            raise ValueError('Problems with text_file')

    lowercase_letter = string.ascii_lowercase
    uppercase_letter = string.ascii_uppercase

    model = {i: 0 for i in lowercase_letter}

    for line in text_file:
        if arguments['text_file'] is None and (line == 'exit' or line == 'exit\n'):
            break
        for i in line:
            if i in lowercase_letter:
                model[i] += 1
            elif i in uppercase_letter:
                model[lowercase_letter[uppercase_letter.find(i)]] += 1

    text_file.close()

    try:
        model_file = open(arguments['model_file'], 'w')
    except:
        raise ValueError('Problems with model_file')

    print(model)

    for i in lowercase_letter:
        if i != 'z':
            model_file.write(str(model[i]) + ',')
        else:
            model_file.write(str(model[i]) + '\n')

    model_file.close()

