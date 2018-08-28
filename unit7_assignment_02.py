__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys

vowels = "aeiou"

def str_till_first_vowel(word):
    ind = 0
    capital = False
    if word[0].isupper():
        capital = True
    word = word.lower()
    for i in word:
        if i in vowels:
            ind = word.index(i)
            break
    return (ind,word[0:ind],capital)

def encrypt(input):
    result = ""
    for i in input:
        end_ind = len(i)
        sp_char = ""
        if not i[end_ind-1].isalpha():
            end_ind = end_ind-1
            sp_char = i[len(i) - 1]
        res = str_till_first_vowel(i)
        encrypt_str = ""
        if res[2] == True:
            encrypt_str+=i[res[0]].swapcase()
        else:
            encrypt_str+=i[res[0]]
        encrypt_str += i[res[0]+1:end_ind]+res[1]
        i = encrypt_str+"ay"+sp_char+" "
        result+=i
    return result.rstrip()

# def test_encrypt():
#     assert "onay" == encrypt(["on"])
#     assert "ellohay" == encrypt(["hello"])
#     assert "ebyay" == encrypt(["bye"])
#     assert "eednay" == encrypt(["need"])


def main(argv = None):
    if argv is None:
        argv = sys.argv
        try:
            try:
                word_list = []
                for i in range(1,len(sys.argv)):
                    word_list.append(sys.argv[i])
            except IndexError:
                raise IndexError
            return encrypt(word_list)
        except Exception as error:
            print(error,file = sys.stderr)
            return 1

if __name__ == "__main__":
    sys.exit(main())