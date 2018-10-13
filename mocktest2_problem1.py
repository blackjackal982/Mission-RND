max_marks = 20

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, then order them lexicographically (case insensitive). For e.g. a comes before b

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.


Note: 
1. use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
2. You can write additional routines as you see fit.
'''
import string
valid_words = string.ascii_uppercase+string.ascii_lowercase+" "

def count_vowel(text):
    vowels ="aeiou"
    count = 0
    for i in text.lower():
        if i in vowels:
            count+=1
    return count

def transform(sentence):
    if type(sentence).__name__!='str':
        raise TypeError
    for i in sentence:
        if i not in valid_words:
            raise ValueError
    sentence = sentence.strip()
    word_list = sentence.split(" ")
    word_list.sort()
    word_list.sort(key = lambda x:count_vowel(x))
    word_list.sort(key = lambda x:len(x),reverse=True)
    text = " ".join(word_list)
    return text.strip()

def test_transform():
    assert "elephant walking runway on" == transform("walking elephant on runway")
    assert transform("how do you feel") =="feel how you do"
    assert ValueError,transform(" 123")
    assert TypeError,transform(0.999)
    assert TypeError,transform()
    assert transform("hello world") == "world hello"
    assert transform(" hello worldsss")== "worldsss hello"
    assert transform("aeb bee") == "aeb bee"
    assert transform("  hello  world   ")=="world hello"
    assert ValueError,transform("hey there??")
    assert transform("aby Gail") == "Gail aby"
