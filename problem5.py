"""
Write a generator function to generate infinite sequence of fibonaci numbers.

0, 1, 1, 2, 3, .......
"""

def fibo():
    first = 0
    second = 1
    count = 0
    while True:
        if count == 0:
            yield(first)
            count+=1
        elif count == 1:
            yield(second)
            count+=1
        else:
            third = first+second
            yield(third)
            first = second
            second = third


# Write your own test cases.

def test_fibo():
    li = []
    a = fibo()
    for i in range(5):
        li.append(next(a))
    assert [0,1,1,2,3] == li

"""
The below function takes an integer and returns boolen True if the given number is fibonaci number else 
return boolean False.

constraints:
1. raise TypeError if number is not an integer.
2. raise ValueError if number is negative.
3. "is_fibo" function should use the above generator.
"""
def is_fibo(number):

    if type(number).__name__ != 'int':
        raise TypeError
    if number<=0:
        raise ValueError
    else:
        a = fibo()
        next_val =next(a)
        if number == next_val:
            return True
        while number>=next_val:
            next_val = next(a)
            if next_val == number:
                return True
            elif next_val>number:
                return False

# Write your own test cases.

def test_is_fibo():
    assert True == is_fibo(5)
    assert True == is_fibo(8)
    assert False == is_fibo(20)
    assert False== is_fibo(77)
    assert False == is_fibo(70)