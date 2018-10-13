__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Wamway is a fictitious company which relies on a pyramid marketing scheme. A set of seed founders start it and start
introducing additional members by referral. There is commission for each referral and for sales of
premium products. This problem focuses on the referral side of the business. The membership fees is 1000Rs.

For every referral, the immediate parent get 10%, grand parent gets 5%, great grand parent 2.5%,
great great grand parent 1.2% and anyone beyond that gets 1%.

E.g. m1 refers m2, and m2 refers m3 and m4.

In the example given, m1 is parent of m2 and m2 is parent of m3 so m1 is grandparent of m3. So if these were the
only referrals, their earnings would be:

m1 earnings: 100 (from m2) + 100 (50 each from m3 and m4) = 200
m2 earnings: 200 (100 each from from m3 and m4) = 200

You are given a file referrals.txt containing the referrals of their first quarter in the following format.

member : referral1, referral2, referral3, ....

Your job is to process the data and use appropriate data structures to give the top k earners and their earnings
in the quarter.

For this problem you have to consider only the first N lines to simulate various
test cases instead of having multiple input files (ie) treat it is as if the file has only N lines

Additional notes:
- no type checking required
- raise ValueError if N <=0 or K <=0
- sort by earnings descending, don't include folks without earnings (ie) with 0 earnings. If two people
have same earnings, sort alphabetically (case sensitive).
- if K > number of people who earned (say P), just return the P tuples as a list.
- return a list of tuples of the form [(name1, earnings1), (name2, earnings2), ...]

Do not modify the input file in any way.
'''

import inspect
import os

# returns a list of (name, earnings) tuples.
def top_earners(file_name, n, k):
    if n<=0 or k<=0:
        raise ValueError
    f=open(file_name)
    list_of_emp = []
    for i in range(n):
        list_of_emp.append(f.readline())
    print(list_of_emp)


# write your own tests
def test_top_earners():
    print(top_earners("referrals.txt",3,5))


def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)
