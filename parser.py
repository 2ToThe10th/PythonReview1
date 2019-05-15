import argparse
import encode_decode
import hack
import train
import train_short
import hack_short


def parse():
    type_of_cipher = ('caesar', 'vigenere', 'vernam')

    parser = argparse.ArgumentParser(description="cipher utility")
    subparsers = parser.add_subparsers()

    encode_parser = subparsers.add_parser('encode', help='encode your text')
    encode_parser.add_argument('--cipher', required=True, choices=type_of_cipher, help='choose type of cipher')
    encode_parser.add_argument('--key', required=True, help='key for cipher')
    encode_parser.add_argument('--input-file', help='input file')
    encode_parser.add_argument('--output-file', help='output file')
    encode_parser.set_defaults(func=encode_decode.encode_decode)
    encode_parser.set_defaults(type='encode')

    decode_parser = subparsers.add_parser('decode', help='decode your text')
    decode_parser.add_argument('--cipher', required=True, choices=type_of_cipher, help='choose type of cipher')
    decode_parser.add_argument('--key', required=True, help='key for cipher')
    decode_parser.add_argument('--input-file', help='input file')
    decode_parser.add_argument('--output-file', help='output file')
    decode_parser.set_defaults(func=encode_decode.encode_decode)
    decode_parser.set_defaults(type='decode')

    train_parser = subparsers.add_parser('train', help='train system to hack')
    train_parser.add_argument('--text-file', help='input text file')
    train_parser.add_argument('--model-file', required=True)
    train_parser.set_defaults(func=train.train)

    hack_parser = subparsers.add_parser('hack', help='decode text without key')
    hack_parser.add_argument('--cipher', default='vigenere', choices=type_of_cipher[:2], help='choose type of cipher')
    hack_parser.add_argument('--input-file', help='input file')
    hack_parser.add_argument('--output-file', help='output file')
    hack_parser.add_argument('--model-file', required=True)
    hack_parser.set_defaults(func=hack.hack)

    train_short_parser = subparsers.add_parser('train-short',
                                               help='this train function better work with small text, because remember words from model text')
    train_short_parser.add_argument('--text-file', help='input text file')
    train_short_parser.add_argument('--model-file', required=True)
    train_short_parser.add_argument('-N', action='store', type=int, required=True)
    train_short_parser.set_defaults(func=train_short.train_short)

    hack_short_parser = subparsers.add_parser('hack-short',
                                              help='this hack function work with model-file made by train-short function')
    hack_short_parser.add_argument('--input-file', help='input file')
    hack_short_parser.add_argument('--output-file', help='output file')
    hack_short_parser.add_argument('--model-file', required=True)
    hack_short_parser.set_defaults(func=hack_short.hack_short)

    return vars(parser.parse_args())
