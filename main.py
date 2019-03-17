import sys
import parser
import encode
import decode
import string

arguments = parser.parse()

if arguments['type'] in ['encode', 'decode'] and arguments['cipher'] in ['caesar', 'vigenere']:
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
            raise ValueError('Bad key');

        if key < 0 or key >= len(string.ascii_lowercase):
            raise ValueError('Bad key');

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
