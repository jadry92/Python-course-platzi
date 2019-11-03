# -*- coding: utf-8 -*-

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    global KEYS
    words = message.split(' ')
    words_cypher = []

    for word in words:
        word_cypher = ''
        for letter in word:
            word_cypher += KEYS[letter]
        words_cypher.append(word_cypher)

    return ' '.join(words_cypher)


def decipher(message_cypher):
    global KEYS
    words = message_cypher.split(' ')
    words_decipher = []

    for word in words:
        word_decipher = ''
        for letter in word:
            for key, value in KEYS.items():
                if letter == value:
                    word_decipher += key

        words_decipher.append(word_decipher)

    return ' '.join(words_decipher)


def run():
    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Inserte su mensaje: '))
            message_cypher = cypher(message)
            print('Mensaje cifrado: {}'.format(message_cypher))
        elif command == 'd':
            message = str(input('Inserte su mensaje: '))
            message_cypher = decipher(message)
            print('Mensaje decifrado: {}'.format(message_cypher))
        elif command == 's':
            print('Fin')
            break
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
