__author__ = 'Kalyan'

max_marks = 30

problem_notes ='''
This problem deals with a custom encryption/decryption scheme that works as follows. 

Given a string like "how are you?" and m * n grid. The characters of the string are filled 
into the grid row wise top to bottom. So for 3 * 5 you get

h o w _ a
r e _ y o
u ? * * *

In the above example _ is shown visually where there is a space character. Unfilled cells are filled with *'s

The encrypted string is found by starting at a specified corner and going clockwise in 
a decreasing spiral till all the cells are covered. So if corner is top right you get "ao***?urhow y e"


Notes:
1. raise TypeError if text is not a str or key is not EncryptKey
2. raise ValueError if the grid cannot accomodate the text  or if rows/cols are <= 0 
3. returns the encrypted string as specified above.
4. see the definitions for Corner and EncryptKey in mock1common.py
'''

from mock1common import EncryptKey, Corner


def text_spiral(m, n, a,dir):
    #top most row
    top = 0
    #bottom most row
    bottom = m-1
    #first col
    left = 0
    #last col
    right = n-1

    e_text = ""
    if dir == Corner.TOP_LEFT:
        direction = 1
        #left to right movement
    elif dir == Corner.TOP_RIGHT:
        direction = 2
        #top to bottom movement
    elif dir == Corner.BOTTOM_RIGHT:
        direction = 3
        #right to left movement
    elif dir == Corner.BOTTOM_LEFT:
        direction = 4
        #bottom to top movement
    while(top<=bottom and left<=right):
        if direction == 1:
            if len(e_text) == (m*n):
                break
            for i in range(left,right+1):
                e_text+=a[top][i]
            print("l to r:"+e_text)
            top=top+1
            direction = 2
        if direction == 2:
            if len(e_text) == (m*n):
                break
            for i in range(top,bottom+1):
                e_text+=a[i][right]
            print("t to b:"+e_text)
            right = right -1
            direction =3
        if direction == 3:
            if len(e_text) == (m*n):
                break
            for i in range(right,left-1,-1):
                e_text+=a[bottom][i]
            print("r to l:"+e_text)
            bottom = bottom -1
            direction = 4
        if direction == 4:
            if len(e_text) == (m*n):
                break
            for i in range(bottom,top-1,-1):
                e_text+=a[i][left]
            print("b to t:"+e_text+str(top))
            left = left+1
            direction = 1
    print(e_text)
    return e_text


def encrypt(text, key):
    if type(text).__name__!='str' or  type(key).__name__!='EncryptKey':
        raise TypeError
    if key.rows <=0 or key.cols<=0 :
        raise ValueError
    if (key.rows*key.cols) < len(text):
        raise ValueError
    matrix = []
    k = 0
    for i in range(key.rows):
        mat = []
        for j in range(key.cols):
            try:
                mat.append(text[k])
                k = k+1
            except IndexError:
                mat.append('*')
        matrix.append(mat)

    encrypt = text_spiral(key.rows,key.cols,matrix,key.corner)
    return encrypt

# a basic test is given, write your own tests based on constraints.
def test_encrypt():
    assert "ao***?urhow y e" == encrypt("how are you?", EncryptKey(3, 5, Corner.TOP_RIGHT))
    assert "how  ?uoyare" == encrypt("how are you?",EncryptKey(3,4,Corner.TOP_LEFT))
    assert "rohello*dl w"== encrypt("hello world",EncryptKey(3,4,Corner.BOTTOM_LEFT))
    assert "**?lhel o" == encrypt("hello ?",EncryptKey(3,3,Corner.BOTTOM_RIGHT))
    assert TypeError, encrypt(123,EncryptKey(4,5,Corner.BOTTOM_RIGHT))
    assert ValueError,encrypt("hey there how are you",EncryptKey(10,-10,Corner.BOTTOM_RIGHT))
    assert "?urhey the g****** e howniod"== encrypt("hey there how u doing?",EncryptKey(4,7,Corner.BOTTOM_LEFT))
    assert ValueError, encrypt("hello world !!", EncryptKey(3, 3, Corner.TOP_RIGHT))
    assert ValueError,encrypt("hello world!!",EncryptKey(-3,-3,Corner.TOP_LEFT))
    assert TypeError ,encrypt("ehllo !!",EncryptKey(3,3,123))
