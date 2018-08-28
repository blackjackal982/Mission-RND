__author__ = 'Kalyan'

max_marks = 20

notes = '''
This is the counterpart to the encrypt routine that you wrote in problem 3. 

You are given the encrypted string, the original key used to encrypt the original string.

Your job is to reconstruct the original string.

Notes:
1. raise TypeError if text is not a str or key is not EncryptKey
2. raise ValueError if the grid is invalid (ie) cannot accomodate the text  or if rows/cols are <= 0 
3. returns the original string (remove the padding chars).
4. You can assume that the original string does not contain the padding chars
5. see the definitions for Corner and EncryptKey in mock1common.py

'''

from mock1common import EncryptKey, Corner

def decrypt(encrypted_text, key):
    if type(encrypted_text).__name__!='str' or type(key).__name__!='EncryptKey':
        raise TypeError
    if key.rows<=0 or key.cols<=0:
        raise ValueError
    ind = 0
    matrix = []
    for i in range(key.rows):
        mat = []
        for j in range(key.cols):
            mat.append(0)
        matrix.append(mat)
    # top most row
    top = 0
    # bottom most row
    bottom = key.rows - 1
    # first col
    left = 0
    # last col
    right = key.cols - 1
    if key.corner == Corner.TOP_LEFT:
        direction = 1
        # left to right movement
    elif key.corner == Corner.TOP_RIGHT:
        direction = 2
        # top to bottom movement
    elif key.corner == Corner.BOTTOM_RIGHT:
        direction = 3
        # right to left movement
    elif key.corner == Corner.BOTTOM_LEFT:
        direction = 4
        # bottom to top movement
    while (top <= bottom and left <= right):
        if direction == 1:
            for i in range(left, right + 1):
                try:
                    matrix[top][i]= encrypted_text[ind]
                except IndexError:
                    pass
                ind = ind+1
            top = top + 1
            direction = 2
        if direction == 2:
            for i in range(top, bottom+1):
                try:
                    matrix[i][right]= encrypted_text[ind]
                except IndexError:
                    pass
                ind = ind+1
            right = right - 1
            direction = 3
        if direction == 3:
            for i in range(right, left-1, -1):
                try:
                    matrix[bottom][i]=encrypted_text[ind]
                except IndexError:
                    pass
                ind = ind+1
            bottom = bottom - 1
            direction = 4
        if direction == 4:
            for i in range(bottom, top-1, -1):
                try:
                    matrix[i][left]=encrypted_text[ind]
                except IndexError:
                    pass
                ind = ind+1
            left = left + 1
            direction = 1
    text = ""
    for i in range(key.rows):
        for j in range(key.cols):
            if matrix[i][j]!='*':
                text+=matrix[i][j]
    print(text)
    return text


# a basic test is given, write your own tests based on constraints.
def test_decrypt():
    assert "how are you?" == decrypt("ao***?urhow y e", EncryptKey(3, 5, Corner.TOP_RIGHT))
    assert decrypt("ao***?urhow y e", EncryptKey(3, 5, Corner.TOP_RIGHT)) == "how are you?"
    assert decrypt("how  ?uoyare" , EncryptKey(3, 4, Corner.TOP_LEFT))== "how are you?"
    assert decrypt("rohello*dl w" , EncryptKey(3, 4, Corner.BOTTOM_LEFT))== "hello world"
    assert decrypt("**?lhel o", EncryptKey(3, 3, Corner.BOTTOM_RIGHT)) == "hello ?"
    assert TypeError, decrypt(123, EncryptKey(4, 5, Corner.BOTTOM_RIGHT))
    assert ValueError, decrypt("hey there how are you", EncryptKey(10, -10, Corner.BOTTOM_RIGHT))
    assert decrypt("?urhey the g****** e howniod" , EncryptKey(4, 7, Corner.BOTTOM_LEFT))== "hey there how u doing?"
    assert ValueError, decrypt("**meraspirplbol ", EncryptKey(3, 3, Corner.TOP_RIGHT))
    assert ValueError, decrypt("h?****aaol!!", EncryptKey(-3, -3, Corner.TOP_LEFT))
    assert TypeError, decrypt("ehllo !!", EncryptKey(3, 3, 123))
    assert "spiral problem" == decrypt("**meraspirplbol ",EncryptKey(4,4,Corner.BOTTOM_RIGHT))
    assert "spiral problem" == decrypt("eraspirpl**mol b",EncryptKey(4,4,Corner.BOTTOM_LEFT))
    assert "sai sirisha!"==decrypt(" i!ahsssairi",EncryptKey(3,4,Corner.TOP_RIGHT))