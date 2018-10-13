__author__ = 'Kalyan'

max_marks = 25  # encrypt -> 13, decrypt 12

problem_notes = '''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''
import string
valid_words = string.ascii_uppercase+string.ascii_lowercase
def gen(number):
    count = 0
    while True:
        yield count
        if count == number-1:
            count = 0
        else:
            count = count+1

def text_map(text,key):
    list_l = []
    a = gen(len(key))
    for i in text:
        if i in valid_words:
            ind = next(a)
            list_l.append(ord(key[ind]) - ord('a'))
        else:
            list_l.append(i)
            continue
    return list_l

# do type checking, non-str should raise TypeException
def encrypt(text, key):
    if type(text).__name__!='str' or type(key).__name__!='str':
        raise TypeError
    for i in key:
        if i not in valid_words:
            raise ValueError
    list_l = text_map(text,key)
    res = ""
    for i in range(len(text)):
        if text[i] in valid_words:
            j = chr(ord(text[i])+list_l[i])
            if text[i].isupper() and j>'Z':
                j = chr(ord(j)-26)
            if text[i].islower() and j>'z':
                j = chr(ord(j)-26)
            res += j
        else:
            res += list_l[i]
    return res


def decrypt(text, key):
    if type(text).__name__!='str' or type(key).__name__!='str':
        raise TypeError
    for i in key:
        if i not in valid_words:
            raise ValueError
    list_l = text_map(text,key)
    res = ""
    for i in range(len(text)):
        if text[i] in valid_words:
            j = chr(ord(text[i])-list_l[i])
            if text[i].islower() and j<'a':
                j = chr(ord(j)+26)
            if text[i].isupper() and j<'A':
                j = chr(ord(j)+26)
            res += j
        else:
            res += list_l[i]
    return res


def test_encrypt():
    assert "hj vkirf" == encrypt("hi there", "abcde")
    assert TypeError,encrypt("")
    assert "hj Vkirf" == encrypt("hi There","abcde")
    assert ValueError,encrypt("hi there","")
    assert "hfnos"==encrypt("hello","abcde")
    assert encrypt("hello","bc") == "igmnp"
    assert ValueError,encrypt(" "," ")
    assert encrypt("abcde","abcde") == "acegi"
    assert ValueError,encrypt("abcde","abc..")
    assert encrypt("abc","a") == "abc"
    assert encrypt("abc","z")=="zab"
    #assert encrypt("ABC","Z")=="ZAB"
    print(encrypt("ABC","Z"))

def test_decrypt():
    assert "hi there" == decrypt("hj vkirf", "abcde")
    assert TypeError,decrypt()
    assert decrypt("hj Vkirf","abcde") == "hi There"
    assert decrypt("hfnos","abcde") =="hello"
    assert decrypt("igmnp","bc") == "hello"
    assert ValueError,decrypt(" "," ")
    assert decrypt("acegi","abcde") == "abcde"
    assert ValueError,decrypt("abcde","abc..")
    assert decrypt("abc","a") == "abc"
    assert decrypt("abc","z")
    assert ValueError,decrypt("abcde",None)
    assert decrypt("zab","z") == "abc"


