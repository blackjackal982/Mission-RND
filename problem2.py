__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
 This is custom encryption scheme that was in popular use to send secret messages in olden days. In this
 scheme successive letters are written in different lines by hand and all the characters are merged line by line
 to create the final encrypted text. The number of lines can differ and is an input to this problem.

 Write encode routine for this cipher given a text and the number of lines n.

 E.g "Hello Cat" with line count 2 when written over 2 lines is:
line1:              H   l   o    C   t
line2:                e   l   ' '  a

    So final text is "HloCtel a" (characters of line 1 followed by characters of line2)

Similarly a word "Popular" with line count 3 will be
line1:            P       l
line2:              o   u   a
line3:                p       r

    So final text is Plouapr

Constraints and notes:
1. Write the cipher routines to work for arbitrary n. Raise value error if n <= 0
2. Assume types are correct
3. Note that the encryption is not done word by word but for the whole text at one go. See the "Hello cat" example, the
   space was treated as part of text and it moved.
4. The problem decomposition is already given for you in the form of 2 routines below. encode must make use of
   get_lines and other python builtin types and features to solve the problem
5. Note that this is a programming problem, don't bother to find out mathematical patterns during the test.
'''

#Implement this generator. Assume n >= 1 as the value checking is done in encode.
def get_lines(n):

    """
    This is an infinite generator returns which line the next character should go to (ie)
    it returns next lines numbers infinitely. For n = 3, it will return 1,2,3,2,1,2,3,2,1,...
    in infinite succession.
    """
    if (n <= 0):
        raise ValueError

    count = 1
    flag = 0
    while True:
        yield (count)
        if flag == 0:
            count+=1
            if count == n:
                flag = 1
        elif flag == 1:
            count-=1
            if count == 1:
                flag = 0

# write this routing using the above generator and additional data structures.
def encode(text, n):
    if n<=0:
        raise ValueError
    else:
        char_list = []
        for i in range(n):
            char_list.append(0)
        a = get_lines(n)
        for i in text:
            s = next(a)
            if char_list[s-1] == 0:
                char_list[s-1] = [i]
            else:
                char_list[s-1].append(i)
        string_res = ''
        for i in char_list:
            string_res+="".join(i)
        return string_res

#write your own tests
def test_get_lines():
    a= get_lines(4)
    list_a = []
    for i in range(5):
        list_a.append(next(a))
    b = get_lines(3)
    list_b = []
    for i in range(9):
        list_b.append(next(b))
    assert [1,2,3,4,3] == list_a
    assert [1,2,3,2,1,2,3,2,1] == list_b

# write your own tests.
def test_encode():
    assert "Plouapr" == encode("Popular", 3)
    assert "HloCtel a" == encode("Hello Cat",2)
    assert "SraiiiSsa h"== encode("Sai Sirisha",4)
