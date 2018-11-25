def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        return True
    
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"

print("All tests passed")