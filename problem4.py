__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
This problem involves writing an iterator class that implements a CyclicCounter that take a value
and returns values from 0 to value and then down to 0 and then -value and back to 0 infinitely.

For e.g. for bound = 2. the iterator next() cycles through the values
0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2,  ...

Notes:
- implement the methods of the class so that it behaves like an iterator with behavior described above
- a negative value should raise ValueError
- no type checking required.
- you must use a constant amount of memory irrespective of the counter starting value (ie) I should be able to use
  really large values without running out of memory.
'''

class CyclicCounter(object):
    def __init__(self,n):
        self.bound = n
        self.flag = 0
        self.flag_p = 1
        self.start = 0
        self.range = (((self.bound + 1) * 2) - 1)
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.res = self.start
        self.count += 1
        if self.count == self.range:
            self.count = 1
            self.flag_p = self.flag_p*-1

        if self.flag == 0:
            self.start+=1
            if self.start == self.bound:
                self.flag = 1
        elif self.flag == 1:
            self.start -= 1
            if self.start == 0:
                self.flag = 1

        return self.res


# a basic test is given, write your own tests.
def test_counter():
    counter = CyclicCounter(2)

    # test the 1st 5 values
    result = []
    for index, value in enumerate(counter):
        if index == 5:
            break
        result.append(value)
    assert [0, 1, 2, 1, 0] == result

    count_1 = CyclicCounter(3)
    res = []
    # test the 1st 10 values
    for index,value in enumerate(count_1):
        if index == 10:
            break
        res.append(value)
    assert [0,1,2,3,2,1,0,-1,-2,-3] == res
