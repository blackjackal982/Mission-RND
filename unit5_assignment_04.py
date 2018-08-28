__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''

def left_binary_search(input_list, value):
    try:
        if iter(input_list):
            input_list = list(input_list)
    except TypeError:
        raise TypeError
    low = 0
    high = len(input_list) - 1
    flag = 0
    while low <= high:
        mid = (low + high) // 2
        if input_list[mid] == value:
            try:
                if mid == 0:
                    return mid
                if input_list[mid - 1] == value:
                    high = mid - 1
                else:
                    flag = 1
                    return mid
            except:
                flag = 1
                return mid
        elif input_list[mid] < value:
            low = mid + 1
        elif input_list[mid] > value:
            high = mid - 1

    if flag == 0:
        return -1
# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert -1 == left_binary_search((1, 1, 1, 3 , 3 , 3 , 4, 4 , 4 , 4, 4, 7, 8, 8),14)
    assert 0 == left_binary_search([1,1,1,1,1,1,1],1)
    assert -1 == left_binary_search([1, 2, 2, 2, 2, 3, 4, 7, 8, 8],10)
    assert 5 == left_binary_search([1,1,1,1,2,3,3,4,5,9,9],3)
    assert 6 == left_binary_search([1,1,1,1,2,2,3,3,8,8,9],3)
    assert 8 == left_binary_search([1,1,1,1,2,2,3,3,8,8,9],8)
    assert 2 == left_binary_search([3,3,4,4,4,4,4,4,5,6,7,9],4)
    assert 0 == left_binary_search(range(0,10),0)
    assert 3 == left_binary_search("bbbcccddddddeee",'c')

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)
