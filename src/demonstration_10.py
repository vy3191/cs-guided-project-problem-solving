"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # Your code here
    input = input_str.split(" ")
    for i in range(len(input)):
        input[i] = int(input[i])
    new_input = sorted(input)    
    print(str(new_input[len(new_input)-1])+" "+str(new_input[0]))
    return str(new_input[len(new_input)-1])+" "+str(new_input[0])
        
    

max_and_min("1 2 3 4 5")  
max_and_min("1 2 -3 4 5") 
max_and_min("1 9 3 4 -5") 

