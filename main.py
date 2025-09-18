import svenskaOrd
import Ultis

swedishWords = svenskaOrd.swedish_words.copy()
reviewWords = svenskaOrd.swedish_words.copy()

def NormalGrammar(wordList, bIsReview):
    while len(wordList) > 0:
        word = Ultis.RandomWord(swedishWords)
        Ultis.MyPrint(word, reviewWords, bIsReview)

def Main():
    Ultis.Resize()
    NormalGrammar(swedishWords, False)
    NormalGrammar(reviewWords, True)


Main()
