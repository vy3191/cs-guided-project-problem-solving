"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    # Your code here
    if len(input_str) == 1 or len(input_str) == 2:
        print(input_str)
        return input_str
    length = len(input_str)
    if length % 2 == 0:
        middle = int(length / 2)
        print(input_str[middle-1: middle+1])
    else:
        print(input_str[length // 2])

get_middle("test")  
get_middle("testing") 
get_middle("middle")  
get_middle("A")   
            
        


