__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if type(first).__name__ != 'str' or type(second).__name__!='str':
        return False
    elif first == "" or second == "":
        return False
    else:
        di = {}
        flag = 0
        first = first.lower()
        second = second.lower()
        first = first.replace(" ","")
        second = second.replace(" ","")
        for i in first:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1
        for i in second:
            if i in di:
                di[i]-=1
            else:
                flag = -1
        for i in di:
            if di[i] != 0:
                flag = -1
                break
        if flag == -1:
            return False
        else:
            return True

# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert True == are_anagrams("anagram","nag a ram")
    assert False == are_anagrams("brain","rain")
    assert False == are_anagrams(None,None)
    assert True == are_anagrams("123","321")
    assert True == are_anagrams("roast beef","eat for BSE")
    assert False == are_anagrams("",None)
    assert False == are_anagrams("","")
    assert False ==are_anagrams(123,None)

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
