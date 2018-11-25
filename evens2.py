def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        evens = 0
        
    for x in numbers:
        if x % 2 == 0:
            evens +=1
            
    return evens % 2 == 0
    
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"

print("All tests passed")