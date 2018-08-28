__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
#from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.

def prune_either_or(sentence):
    if type(sentence).__name__ !='str':
        return sentence
    result = ''
    str1 = 'either '
    str2 = ' or '
    try:
        eith_ind = sentence.index(str1)
        or_ind = sentence.index(str2)
        if eith_ind < or_ind and sentence[eith_ind-1]==' ' and sentence.count(" or ") == 1 and sentence.count(" either ")==1 and (or_ind-(eith_ind+len("either"))>0):
            i = 0
            str1 = str1.replace(" ","")
            str2 = str2.replace(" ","")
            if sentence.index(str1) == 0 :
                return sentence
            elif str1 in sentence and str2 in sentence:
                while i < len(sentence):
                    if not sentence[i].isspace():
                        word_form = ''
                        while not sentence[i].isspace():
                            word_form+=sentence[i]
                            i = i+1
                        if word_form != str1 and word_form !=str2:
                            result+=word_form
                        if word_form == str2:
                            break
                    else:
                        i = i+1
                        if word_form != str1:
                            result+=' '

                return result.rstrip()
        else:
            return sentence
    except ValueError:
        return sentence


def test_prune_either_or_student():
    assert "Either we would go holiday or movie" == prune_either_or("Either we would go holiday or movie")
    assert "He drinks coffee" == prune_either_or("He drinks either coffee or tea")
    assert "Hello! you are neither mad or dumb" == prune_either_or("Hello! you are neither mad or dumb")
    assert "We are good"== prune_either_or("We are either good or we are assumming")
    assert "Two mythical cities eitheron and oregon" == prune_either_or("Two mythical cities eitheron and oregon")
    assert "i go neither movie not play or healthy" == prune_either_or("i go neither movie not play or healthy")
    assert 123 ==  prune_either_or(123)
    assert None == prune_either_or(None)
    assert "is either or replace" == prune_either_or("is either or replace")

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
