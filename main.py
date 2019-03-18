import sys
import parser
import hack
import encode
import decode
import string


def main():
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
                input_file.close()
                raise ValueError('Problems with output_file')

        if arguments['cipher'] == 'vigenere':
            key = arguments['key'].lower()

            for i in key:
                if i not in string.ascii_lowercase:
                    input_file.close()
                    output_file.close()
                    raise ValueError('Bad key');

            encode_fun = encode.encode_vigenere
            decode_fun = decode.decode_vigenere
        else:

            try:
                key = int(arguments['key'])
            except:
                input_file.close()
                output_file.close()
                raise ValueError('Bad key')

            if key < 0 or key >= len(string.ascii_lowercase):
                input_file.close()
                output_file.close()
                raise ValueError('Bad key')

            encode_fun = encode.encode_caesar
            decode_fun = decode.decode_caesar

        key_index = 0

        if arguments['type'] == 'encode':
            for line in input_file:
                if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                    break
                return_value = encode_fun(line, key, key_index)
                output_file.write(return_value[0])
                key_index = return_value[1]
                output_file.flush()
        else:
            for line in input_file:
                if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                    break
                return_value = decode_fun(line, key, key_index)
                output_file.write(return_value[0])
                key_index = return_value[1]
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
                input_file.close()
                raise ValueError('Problems with output_file')

        key = arguments['key']

        code_string = string.ascii_uppercase + string.ascii_lowercase + string.digits + ',.'

        code_index = 0

        out_text = []

        for line in input_file:
            if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                break
            for i in line:

                if i not in code_string:
                    out_text.append(i)
                else:
                    if code_index >= len(key):
                        input_file.close()
                        output_file.close()
                        raise ValueError('Too small key')
                    out_text.append(code_string[(code_string.find(i)
                                                 ^ code_string.find(key[code_index]))])
                    code_index += 1

        output_file.write(''.join(out_text))
        input_file.close()
        output_file.close()

    if arguments['type'] == 'train':

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

        for i in lowercase_letter:
            if i != 'z':
                model_file.write(str(model[i]) + ',')
            else:
                model_file.write(str(model[i]) + '\n')

        model_file.close()

    if arguments['type'] == 'hack' and arguments['cipher'] == 'vigenere':
        if arguments['input_file'] is None:
            input_file = sys.stdin
            print('Input from stdin.\nTo exit programme type "exit"')
        else:
            try:
                input_file = open(arguments['input_file'], 'r')
            except:
                raise ValueError('Problems with input_file')

        input_text = []

        lowercase_letter = string.ascii_lowercase
        uppercase_letter = string.ascii_uppercase

        full_input_text = []

        for line in input_file:
            if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                break
            full_input_text.append(line)
            for i in line:
                if i in lowercase_letter:
                    input_text.append(i)
                elif i in uppercase_letter:
                    input_text.append(lowercase_letter[uppercase_letter.find(i)])

        input_file.close()

        string_input_text = ''.join(input_text)

        try:
            model_file = open(arguments['model_file'], 'r')
        except:
            raise ValueError('Problems with model_file')

        try:
            train_model = [int(i) for i in model_file.readline().split(',')]
        except:
            raise TypeError('Wrong model_file')

        if len(train_model) != len(lowercase_letter):
            raise ValueError('Wrong model_file')

        model_file.close()

        match_index_in_model = 0
        count_of_letters_in_model = 0

        for i in train_model:
            match_index_in_model += max(0, i * (i - 1))
            count_of_letters_in_model += i

        match_index_in_model /= max(1, count_of_letters_in_model * (count_of_letters_in_model - 1))

        len_of_key = 0

        for len_of_key in range(1, len(input_text)):
            all_match_index = []

            for first_element in range(len_of_key):
                model_of_hack = {i: 0 for i in lowercase_letter}

                for i in range(first_element, len(string_input_text), len_of_key):
                    model_of_hack[ string_input_text[i] ] += 1

                match_index_in_input = 0
                count_of_letters_in_input = 0

                for i in model_of_hack.values():
                    match_index_in_input += max(0, i * (i - 1))
                    count_of_letters_in_input += i

                match_index_in_input /= max(1, count_of_letters_in_input
                                            * (count_of_letters_in_input - 1))

                all_match_index.append(match_index_in_input)

            if all([(i > match_index_in_model*0.8) for i in all_match_index]):
                break

        list_key = []

        for i in range(len_of_key):
            list_key.append(lowercase_letter[hack.hack_caesar(string_input_text[i::len_of_key], train_model)])

        key = ''.join(list_key)

        if arguments['output_file'] is None:
            output_file = sys.stdout
        else:
            try:
                output_file = open(arguments['output_file'], 'w')
            except:
                raise ValueError('Problems with output_file')

        key_index = 0

        for line in full_input_text:
            return_value = decode.decode_vigenere(line, key, key_index)
            output_file.write(return_value[0])
            key_index = return_value[1]
            output_file.flush()

        output_file.close()

    if arguments['type'] == 'hack' and arguments['cipher'] == 'caesar':
        if arguments['input_file'] is None:
            input_file = sys.stdin
            print('Input from stdin.\nTo exit programme type "exit"')
        else:
            try:
                input_file = open(arguments['input_file'], 'r')
            except:
                raise ValueError('Problems with input_file')

        input_text = []

        lowercase_letter = string.ascii_lowercase
        uppercase_letter = string.ascii_uppercase

        full_input_text = []

        for line in input_file:
            if (line == 'exit\n' or line == 'exit') and arguments['input_file'] is None:
                break
            full_input_text.append(line)
            for i in line:
                if i in lowercase_letter:
                    input_text.append(i)
                elif i in uppercase_letter:
                    input_text.append(lowercase_letter[uppercase_letter.find(i)])

        input_file.close()

        string_input_text = ''.join(input_text)


        try:
            model_file = open(arguments['model_file'], 'r')
        except:
            raise ValueError('Problems with model_file')

        try:
            train_model = [int(i) for i in model_file.readline().split(',')]
        except:
            raise TypeError('Wrong model_file')

        if len(train_model) != len(lowercase_letter):
            raise ValueError('Wrong model_file')

        model_file.close()

        key = hack.hack_caesar(string_input_text, train_model)

        if arguments['output_file'] is None:
            output_file = sys.stdout
        else:
            try:
                output_file = open(arguments['output_file'], 'w')
            except:
                raise ValueError('Problems with output_file')

        key_index = 0

        for line in full_input_text:
            return_value = decode.decode_caesar(line, key, key_index)
            output_file.write(return_value[0])
            key_index = return_value[1]
            output_file.flush()

        output_file.close()


if __name__ == '__main__':
    main()

