import datetime

"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""
def data_type(value):
    # Your code here
    if type(value).__name__ == "dict":
        print("dictionary")
        return "dictionary"
    elif type(value).__name__ == "str":
        print("string")
    else:
        print(type(value))
        print(type(value).__name__)
                

data_type([1, 2, 3, 4])
data_type({'key': "value"}) 
data_type("This is an example string.")
data_type(datetime.date(2018,1,1))


