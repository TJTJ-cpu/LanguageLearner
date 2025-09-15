import random
import time
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


def DelayPrint(string, bNewLine = False):
    if bNewLine:
        print()
    stringArr = list(string)
    for i in stringArr:
        time.sleep(0.013)
        print(i, end='', flush=True)

def NewLine(bNewLine = False):
    if bNewLine:
        print()
    newLine = 20 * '-'
    stringArr = list(newLine)
    for i in stringArr:
        time.sleep(0.01)
        print(i, end='', flush=True)


def Resize():
    keyboard.send('ctrl+0')
    for _ in range(50):
        keyboard.send('ctrl+equal')

def MyPrint(lst):
    os.system('cls')
    NewLine()
    DelayPrint(f'English Word: {lst[0]}', True)
    DelayPrint(f'Singular Obestämd: ', True)
    keyboard.wait('space')
    DelayPrint(lst[1])
    DelayPrint(f'Plural Obestämd: ', True)
    keyboard.wait('space')
    DelayPrint(lst[2])
    DelayPrint(f'Singular Bestämd: ', True)
    keyboard.wait('space')
    DelayPrint(lst[3])
    DelayPrint(f'Plural Bestämd: ', True)
    keyboard.wait('space')
    DelayPrint(lst[4])
    NewLine(True)
    keyboard.wait('space')
    os.system('cls')


