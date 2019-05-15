#!/usr/bin/env python3

import parser

if __name__ == '__main__':
    terminal_arguments = parser.parse()
    terminal_arguments['func'](terminal_arguments)
