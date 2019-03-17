import sys
import argparse


def parse():
    parser = argparse.ArgumentParser(description="encoder")
    parser.add_argument('type', action='store', type=str)

    type_of_cipher = ('caesar', 'vigenere', 'vernam')

    if 'encode' == sys.argv[1]:
        parser.add_argument('--cipher', action='store', type=str, required=True, choices=type_of_cipher)
        parser.add_argument('--key', action='store', type=str, required=True)
        parser.add_argument('--input-file', action='store', type=str)
        parser.add_argument('--output-file', action='store', type=str)

    elif 'decode' == sys.argv[1]:
        parser.add_argument('--cipher', action='store', type=str, required=True, choices=type_of_cipher)
        parser.add_argument('--key', action='store', type=str, required=True)
        parser.add_argument('--input-file', action='store', type=str)
        parser.add_argument('--output-file', action='store', type=str)

    elif 'train' == sys.argv[1]:
        parser.add_argument('--text-file', action='store', type=str)
        parser.add_argument('--model-file', action='store', type=str, required=True)

    elif 'hack' == sys.argv[1]:
        parser.add_argument('--cipher', action='store', type=str, required=True, choices=type_of_cipher)
        parser.add_argument('--input-file', action='store', type=str)
        parser.add_argument('--output-file', action='store', type=str)
        parser.add_argument('--model-file', action='store', type=str, required=True)

    else:
        raise ValueError('argument "type" is required')

    return vars(parser.parse_args())

