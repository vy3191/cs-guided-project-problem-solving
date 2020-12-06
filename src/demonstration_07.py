"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def repeat_it(input_str):
    # Your code here
    result = input_str[0].upper()
    count = 1
    for i in range(1,len(input_str)):
        result += "-"+input_str[i].upper()+ (input_str[i].lower()) * count
        count += 1
    print(result)    
    return result   
repeat_it("abcd") 
repeat_it("RqaEzty")
repeat_it("cwAt")
  
        
        
