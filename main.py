import sys
import argparse

parser = argparse.ArgumentParser(description="encoder")
parser.add_argument('type', action='store', type=str)

if 'encode' in sys.argv:
    parser.add_argument('--cipher', action='store', type=str, required=True)
    parser.add_argument('--key', action='store', type=str, required=True)
    parser.add_argument('--input-file', action='store', type=str)
    parser.add_argument('--output-file', action='store', type=str)

elif 'decode' in sys.argv:
    parser.add_argument('--cipher', action='store', type=str, required=True)
    parser.add_argument('--key', action='store', type=str, required=True)
    parser.add_argument('--input-file', action='store', type=str)
    parser.add_argument('--output-file', action='store', type=str)

elif 'train' in sys.argv:
    parser.add_argument('--text-file', action='store', type=str)
    parser.add_argument('--model-file', action='store', type=str, required=True)

elif 'hack' in sys.argv:
    parser.add_argument('--input-file', action='store', type=str)
    parser.add_argument('--output-file', action='store', type=str)
    parser.add_argument('--model-file', action='store', type=str, required=True)
else:
    raise ValueError('argument "type" is required')

print(parser.parse_args())