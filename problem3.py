__author__ = 'Kalyan'

# Score you will get if you pass all the tests.
max_marks = 25

problem_notes = '''
Find the Lowest common multiple of 2 positive numbers which are given in their prime factorized form defined in problem1

You must return the result in a valid prime factorized form as described in problem1.
Invalid results will fail the tests, so do pay attention to the definition of a valid factorization given in problem1.

Use python builtins and data types as you see fit.

For HCF and LCM: http://www.whitman.edu/mathematics/higher_math_online/section03.06.html

Notes:
1. Assume inputs are valid and of the the right type.
2. first and second are list of tuples which represent a number and they are in prime factorized form as described in
   problem1
3. Do not convert the list into a number and then do ordinary math with it :). Deal with the factorized forms directly.
   See the above link.
'''

def get_lcm(first, second):
    result = []
    if first == [] and second == []:
        return result
    if first == []:
        return second
    if second == []:
        return first
    first_fact = {}
    second_fact = {}
    for (i, j) in first:
        first_fact[i] = j
    for (i, j) in second:
        second_fact[i] = j
    match_factor = {k: max(first_fact[k], second_fact[k]) for k in first_fact if k in second_fact}
    unmatch_factor1 = {k: second_fact[k] for k in set(second_fact) - set(first_fact)}
    unmatch_factor2 = {k: first_fact[k] for k in set(first_fact) - set(second_fact)}
    unmatch_factor1.update(unmatch_factor2)
    match_factor.update(unmatch_factor1)
    for i in match_factor:
        result.append((i, match_factor[i]))
    result.sort()
    return result

# some basic tests given, write more according to given constraints.
def test_get_lcm():
    assert [(2,1), (5,1)] == get_lcm([(2,1)], [(5,1)])
    assert [(3,2)] == get_lcm([], [(3,2)]) # empty list is 1
    assert [(3, 1), (5, 1), (7, 1)] == get_lcm([(3, 1), (5, 1)], [(3, 1), (7, 1)])
