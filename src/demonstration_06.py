"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    vowels = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True
    }
    count = 0
    for char in input_str:
        if char not in vowels:
            continue
        count += 1
    print(count)    
    return count  

get_count("abcedfghijklm") 
get_count("venky")
get_count("apple")
get_count("mangoes")
 

