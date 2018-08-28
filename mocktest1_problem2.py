__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Return the n most frequently occurring chars and their respective counts
e.g cccaaaaabbbb, 2 should return [(a 5) (b 4)]
in case of a tie, return char which comes earlier in alphabet ordering (capitals before smalls)
e.g. cdbba,2 -> [(b,2) (a,1)]
use standard types and and builtin functions we have used in the course.

constraints:
1. raise TypeError if word is not a str or n is not an int
2. raise ValueError if n <= 0,
3. if n > number of unique chars return the available chars and 
   their counts (sorted by above criteria)
4. The function should be case sensitive (ie) A and a are different. 
   So aaAABBB, 2 should return [(B,3), (A,2)]
'''
from itertools import groupby
import string
def _freq_groupby(data):
    freq_list = [(k,len(list(g))) for k, g in groupby(data)]
    return freq_list

def most_frequent(word, n):
    if type(word).__name__!='str' or type(n).__name__!='int':
        raise TypeError
    if word == None or word == "":
        return None
    if n<=0:
        raise ValueError
    else:
        res = []
        list_rep = _freq_groupby(word)
        list_rep.sort(key= lambda x:x[1])
        list_rep.reverse()
        for i in range(n):
            res.append(list_rep[i])
        return res

#write your own tests.
def test_most_frequent():
    assert [('a',5),('b',4)] == most_frequent("aaaaabbbbcccdde", 2)
    assert [('1',5),('2',4),('3',3)] == most_frequent("1111122223334",3)
    assert None ==  most_frequent("",1)
    assert ValueError ,most_frequent("abcd",-1)
    assert TypeError,most_frequent(120,2)
    assert TypeError,most_frequent("abcd",'2')
    assert [('b',5),('A',3)] == most_frequent("abbbbbAAAc",2)