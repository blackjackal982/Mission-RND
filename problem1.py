__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Return the top n most frequently occurring chars and their respective counts in a given string.

e.g "aaaaabbbbccc", 2 should return [('a', 5) ('b', 4)]

in case of a tie, return char which comes later in alphabet ordering first
e.g. "cdbba",2 -> [('b',2), ('d',1)]
     'cdbba',3 -> [('b',2), ('d',1), ('c',1)]

use standard types and and builtin functions we have used in the course.

constraints:
1. raise TypeError if word is not a str or n is not an int
2. raise ValueError if n <= 0,
3. if n > number of unique chars just return the available chars and their counts
4. The function should be case sensitive (ie) A and a are different. So 'aAABBB', 2 should return [('B',3), ('A',2)]
'''

def _freq_groupby(word):
    d = []
    for i in word:
        if i not in d:
            d.append((i,word.count(i)))
    return list(set(d))


def top_chars(word, n):
    if type(word).__name__!='str' or type(n).__name__!='int':
        raise TypeError
    if word == None or word == "":
        return None
    if n<=0:
        raise ValueError
    else:
        res = []
        list_rep = _freq_groupby(word)
        list_rep.sort(key=lambda x: x[1])
        list_rep.reverse()
        for i in range(n):
            res.append(list_rep[i])
        return res

#write your own tests.
def test_top_chars():
    assert [('a', 5), ('b', 4)] == top_chars("aaaaabbbbcccdde", 2)
    assert [('1', 5), ('2', 4), ('3', 3)] == top_chars("1111122223334", 3)
    assert None == top_chars("", 1)
    assert ValueError, top_chars("abcd", -1)
    assert TypeError, top_chars(120, 2)
    assert TypeError, top_chars("abcd", '2')
    assert [('b', 5), ('A', 3)] == top_chars("abbbbbAAAc", 2)
    assert [('B',4),('A',3)] == top_chars("aAAABBBB",2)
    assert [('B',3), ('A',2)]== top_chars('aAABBB', 2 )
    assert top_chars("cdbba",2)==[('b',2), ('d',1)]