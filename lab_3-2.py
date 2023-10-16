"""
Create a Python file named lab_3-2.py
Copy the following examples into a Python file one at a time. 
Think about what kind of error you think it will throw before running the code. 
When you have run one line, be sure to comment it before adding your next line.
After you have commented out a line, add a comment listing what error type occured.
	
 	int(a)
	int('a')
	'a' + 2
	import date
	print("I'm a happy camper!)

"""

# Attempting to convert 'a' to an integer, which is not a valid integer.
# This will raise a Value Error.
int(a)

# Attempting to convert 'a' (a string that doesn't represent a valid integer) to an integer.
# This will raise a Value Error.
int('a')

# Attempting to concatenate a string 'a' with an integer 2.
# This will raise a Type Error because you can't concatenate a string and an integer directly.
'a' + 2

# Attempting to import a module 'date' which does not exist.
# This will raise an Import Error.
import date

# Attempting to print a string with a missing closing quotation mark.
# This will raise a Syntax Error.
print("I'm a happy camper!)
