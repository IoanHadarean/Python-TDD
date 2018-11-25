"""
Solution to the challenge in the `Test After` unit found in the `Test Driven
Development with Python lesson`
NOTE: The solution found in this file is one of the many potential solutions
that can be used to achieve the end result expected by the challenge in the
lesson.
"""

def count_upper_case(message):
    
    """
    Count the number of upper case characters in a given message
    `message` is the piece of text to be checked
    
    Returns the number of uppercase characters in a message
    """
    
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One uppercase"
assert count_upper_case("a") == 0, "One lowercase"
assert count_upper_case("£$%%>") == 0, "Special characters"
assert count_upper_case("A$£") == 1, "Uppercase and special characters"
assert count_upper_case("AA") == 2, "Multiple uppercase"
 
    
print("All tests passed")