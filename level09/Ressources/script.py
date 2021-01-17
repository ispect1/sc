#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Введите файл, который нужно распарсить')
        sys.exit()

    try:
        with open(sys.argv[1], 'rb') as f:
            old_line = f.read().strip()
            line = ''
            for i, ch in enumerate(old_line):
                line = line + chr((ch - i) % 255)
        print(f'Password: {line}')
    except:
        print('Invalid parse file')
