#!/usr/bin/env python3
import sys
import json


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Введите файл, который нужно распарсить')
        sys.exit()

    try:
        with open(sys.argv[1]) as f:
            pcap = json.load(f)
        line = [bytes.fromhex(p['_source']['layers']['data']['data.data'].replace(':', '')) for p in pcap]
        byte = b''
        for b in line:
            byte = byte + b
        print('Dump:\t', byte, '\n')
        byte = byte[byte.find(b'Password'):]
        byte = byte[:byte.find(b'\x00')].strip()

        i = 0
        while True:
            try:
                if hex(byte[i]) == '0x7f':
                    byte = byte[:i - 1] + byte[i + 1:]
                    i -= 1
                else:
                    i += 1

            except IndexError:
                break

        print(f'{byte.decode()}')
    except:
        print('Invalid parse file')
