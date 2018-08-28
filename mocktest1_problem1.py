__author__ = 'Kalyan'

max_marks = 25

problem_notes ='''
Write a routine to sort the given list of numbers according to the number
of prime factors it has.

Constraints:
1. 1 and 0 are considered to have 0 factors
2. For negative numbers, the factor count of the corresponding
   positive numbers is considered for sorting
3. Numbers with more factors come before numbers with fewer factors
4. In case of a tie, bigger numbers (numerically) comes first
5. Return a new sorted list of numbers (not-inplace)
6. Refer to the testcase for an example.

Notes:
1. Use the python built in sorting functionality to get this done.
2. Write additional helper routines as required.
3. Assume that input is valid list of numbers.
'''
def factorize_number(number):
    if number < 0:
        number = number*-1
    elif type(number).__name__!="int":
        raise TypeError
    if number == 1 or number == 0:
        return 0
    else:
        factors =[]
        if number == 2:
            return 1
        else:
            i=2
            while i  <= number:
                while number % i == 0:
                    number = number // i
                    factors.append(i)
                i = i + 1
        return len(set(factors))

# assume numbers is a valid list of numbers
def sort_by_factor_count(numbers):
    if iter(numbers):
        numbers = list(numbers)
    factor_len = []
    for i in numbers:
        factor_len.append(factorize_number(i))
    new_list = [(-x, y) for x, y in sorted(zip(factor_len, numbers))]
    new_list.reverse()
    res = [x[1] for x in new_list]
    return res


# one basic test given, write more exhaustive tests
def test_sort_by_factor_count():
    # 10 has 2 factors [2,5] , 6 has 2 [2,3], 8 has 1 [2] and 2 has 1 [2], hence the result
    assert [10, 6, 8, 2] == sort_by_factor_count([2, 8, 6, 10])
    assert [10,4,3,-1] == sort_by_factor_count([-1,3,4,10])
    assert [18,17,16,13] == sort_by_factor_count([16,17,18,13])
    assert [4,2,1,0]== sort_by_factor_count([0,1,2,4])
    assert [18,12,19,17] == sort_by_factor_count((12,17,18,19))
    assert [-6,-4] == sort_by_factor_count([-4,-6])