def number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    """
    Test that two values are equal. Raises AssertionError if both values are
    not equal.
    `actual` is the actual value produced
    `expected` is the value that was supposed to be produced
    """
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    """
    Test that two values are not equal. Raises AssertionError if both values
    are not equal.
    `a` is the actual value produced
    `b` is the value that was supposed to be produced
    """
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
def test_is_in(collection, item):
    """
    Check to ensure that a given collection contains a given value. Raises
    AssertionError if `item` is not in `collection`
    `collection` is the collection to be tested
    `item` is the item that is being searched for
    """
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
#test_are_equal(number_of_evens([1,2,3,4,5]), 2) 
    
#test_not_equal(number_of_evens([1,2,3,4,5]), 0)

test_is_in(["fruit", "banana"], "apple")