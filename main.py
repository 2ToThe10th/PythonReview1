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

    x = 0

    lowercase_letters = string.ascii_lowercase

    if arguments['cipher'] == 'vigenere':
        key = arguments['key'].lower()
        if ''.join(sorted(key)) != lowercase_letters:
            raise ValueError('Bad key')
    else:
        key = lowercase_letters[int(arguments['key']):] + lowercase_letters[:int(arguments['key'])]

    if arguments['type'] == 'encode':
        for line in input_file:
            if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                break
            output_file.write(encode.encode_ces_vig(line, key))
            output_file.flush()
    else:
        for line in input_file:
            if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                break
            output_file.write(decode.decode_ces_vig(line, key))
            output_file.flush()
