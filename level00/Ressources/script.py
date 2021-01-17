import string
import sys


alphabet = string.ascii_lowercase


def decrypt(encrypted_message, key):

    decrypted_message = ""

    for c in encrypted_message:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    return decrypted_message.strip()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Введите файл, который нужно расшифровать')
        sys.exit()

    for key in range(26):
        pwd = decrypt(sys.argv[1], key)
        print(pwd)
