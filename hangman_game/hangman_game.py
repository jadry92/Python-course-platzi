# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = ['ball',
'massive',
'arrange',
'aunt',
'curly',
'encouraging',
'peace',
'kind',
'overconfident',
'worm',
'dashing',
'excited']


def pick_up_word():
	global WORDS
	idx = random.randint(0, len(WORDS)-1)
	return WORDS[idx]


def display_board(hidden_word, tries, clue='-'):
    global IMAGES
    print(IMAGES[tries])
    print('*****************************')
    print('GUES = {}'.format(''.join(hidden_word)))
    print('*****************************')
    if tries > 5:
        print('CLUE : {}'.format(clue))

def run():
    word = pick_up_word()
    hidden_word = list('-'*len(word))
    tries = 0
    clue = ''
    while True:
        display_board(hidden_word, tries, clue)
        current_letter = str(input('Pick up a letter : '))

        letter_index = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_index.append(idx)

        if len(letter_index) == 0:
            tries +=1
            if tries == 7:
                display_board(hidden_word, tries, clue)
                print(' ')
                print('YOU LOSE')
                print('The word was {}!'.format(word.upper()))
                break
        else:
            for idx in letter_index:
                hidden_word[idx] = current_letter
            letter_index = []

        if tries > 5:
            clue = word[random.randint(0,len(word)-1)]

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('YOU WIN')

def welcome():
	print('Welcome to Hangman GAME')


if __name__ == '__main__':
    welcome()
    run()
