__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''
di = {'a':0,'e':1,'i':2,'o':3,'u':4}
c = {0:'a',1:'e',2:'i',3:'o',4:'u'}
# Notes:,
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].
def numberTobase(number,base):
    if number == 0:
        return [0]
    flag = 0
    digits = []
    if number<0:
        flag = 1
        number=number*-1
    while number:
        digits.append(int(number%base))
        number //= base
    if flag == 0:
        return digits[::-1]
    else:
        return digits[::-1]+['-']

def to_custom_base5(number):
    if type(number).__name__!='int':
        raise TypeError
    digs = numberTobase(number,5)
    text = ""
    if number<0:
        k = 1
    else:
        k = 0
    if k == 1:
        text+='-'
    for i in range(0,len(digs)-k):
        text+=c[digs[i]]
    return text

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.
def from_custom_base5(a):
    if type(a).__name__!="str":
        raise TypeError
    s = a.strip()
    if s=="":
        raise ValueError
    flag = 1
    flag_occ =0
    for i in s:
        if i.isalpha():
            if i.lower() not in "aeiou":
                raise ValueError
        elif i == '+' and flag_occ==0:
            flag_occ =1
        elif i == '-' and flag_occ==0:
            flag = -1
            flag_occ=1
        else:
            raise ValueError
    if flag_occ != 0:
        r  = s[1:]
        rev = r[::-1]
    else:
        rev = s[::-1]
    sum = 0
    for i in range(len(rev)):
        sum = sum+di[rev[i]]*5**i
    return sum*flag

# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ia" == to_custom_base5(10)
    assert "-ia"==to_custom_base5(-10)
    try:
        to_custom_base5("=1")
    except TypeError:
        pass

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("ia")
    assert -10 == from_custom_base5("-ia")
    assert 10 == from_custom_base5("+ia")
    assert 10 == from_custom_base5(" +ia ")
    try:
        from_custom_base5("+i a")
    except ValueError:
        pass
    assert 20 == from_custom_base5(to_custom_base5(20))