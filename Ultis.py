import random
import keyboard
import os


def RandomWord(lst):
    if not lst:
        return None, None, None, None
    englishWord = random.choice(list(lst))
    singular = lst[englishWord]['singular']
    plural = lst[englishWord]['plural']
    definiteSingular = lst[englishWord]['definite_singular']
    definitePlural = lst[englishWord]['definite_plural']
    del lst[englishWord]
    return englishWord, singular, plural, definiteSingular, definitePlural


def MyPrint(lst):
    os.system('cls')
    print(20 * '-')
    print(f'English Word: {lst[0]}')
    print(f'Singular: ', end='', flush=True)
    keyboard.wait('space')
    print(lst[1])
    print(f'Plural: ', end='', flush=True)
    keyboard.wait('space')
    print(lst[2])
    print(f'Definite Singular: ', end='', flush=True)
    keyboard.wait('space')
    print(lst[3])
    print(f'Definite Plural: ', end='', flush=True)
    keyboard.wait('space')
    print(lst[4])
    print(20 * '-')
    keyboard.wait('space')
    os.system('cls')


