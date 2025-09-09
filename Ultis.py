import random
import keyboard
import os


def RandomWord(lst):
    if not lst:
        return None, None, None, None
    englishWord = random.choice(list(lst))
    singular = lst[englishWord]['singular']
    plural = lst[englishWord]['plural']
    definite = lst[englishWord]['definite']
    del lst[englishWord]
    return englishWord, singular, plural, definite


def MyPrint(lst):
    print(20 * '-')
    print(f'English Word: {lst[0]}')
    print(f'Svenska Singular: ', end='', flush=True)
    keyboard.wait('space')
    print(lst[1])
    print(f'Svenska Plural: ', end='', flush=True)
    keyboard.wait('space')
    print(lst[2])
    print(f'Svenska Definite: ', end='', flush=True)
    keyboard.wait('space')
    print(lst[3])
    print(20 * '-')
    os.system('cls')
