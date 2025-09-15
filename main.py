import svenskaOrd
import Ultis

swedishWords = svenskaOrd.swedish_words

def NormalGrammar(wordList):
    while len(wordList) > 0:
        word = Ultis.RandomWord(swedishWords)
        Ultis.MyPrint(word)

def Main():
    Ultis.Resize()
    NormalGrammar(swedishWords)



Main()
