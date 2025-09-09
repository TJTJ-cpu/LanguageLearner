import svenskaOrd
import Ultis

swedishWords = svenskaOrd.swedish_words


while len(swedishWords) > 0:
    word = Ultis.RandomWord(swedishWords)
    Ultis.MyPrint(word)

