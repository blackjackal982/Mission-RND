__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''
def repeats(digits):
    if type(digits).__name__!="str":
        raise TypeError
    for i in digits:
        if int(i)<0 or int(i)>9:
            raise ValueError
    digits.strip()
    poss = []
    for i in range(len(digits)):
        for j in range(i+2,len(digits)):
            if digits[i:j] in digits and digits.count(digits[i:j])>=2:
                poss.append((digits[i:j],digits.count(digits[i:j])))
    a = list(set(poss))
    a.sort(key=lambda s:(s[1],int(s[0])),reverse=True)
    return a

def test_repeats():
    try:
        repeats(120)
    except TypeError:
        pass
    assert [("123",2),("23",2),("12",2)]==repeats("1231234")
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")
    try:
        print(repeats("123acb"))
    except ValueError:
        pass
