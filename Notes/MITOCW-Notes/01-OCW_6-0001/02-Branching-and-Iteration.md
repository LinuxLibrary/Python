# Branching and Iteration

- **STRINGS**
	- These are letters, special characters, spaces, digits
	- Enclose in quotation marks or single quotes
	
	```
	>>> hi = "hello there"
	```
	
	- Concatinate strings
	
	```
	>>> name = "ana"
	>>> greet = hi + name
	>>> greeting = hi + " " + name
	```
	
	- Do some operations on a string as defined in Python
	
	```
	>>> silly = hi + (" " + name)* 3
	```
	
	- Another example of concatination
	
	```
	>>> x = 1
	>>> print(x)
	>>> x_str = str(x)
	>>> print("My fav number is", x, ".", "x=", x)
	>>> print("My fav number is", x_str + "." + "x=" + x_str)
	>>> print("My fav number is" + x_str + "." + "x=" + x_str)
	```
	
	- **INPUT/OUTPUT: input("")**
		- Prints whatever in the quotes
		- Binds the user input to a variable
		
		```
		>>> text = 	input("Type anything... ")
		>>> print(5*text)
		```
		
		- `input` gives you a string so you must cast if working with numbers
		
		```
		>>> num = int(input("Type anything... "))
		>>> print(5*num)
		```
		
	- **COMPARISION OPERATORS ON `int`, `float`, `string`**
		- Lets take two variables `i` and `j`
		- Comparisions below evaluate to a Boolean
		
		```
		i > j
		i >= j
		i < j
		i <= j
		i == j --> equality test, True if i is the same as j
		i != j --> inequality test, True if i not the same as j
		```
		
	- **LOGICAL OPERATORS ON bools**
		- `a` and `b` are variables (with Boolean values)
		- `not a` --> True if `a` is `False` | False if `a` is `True`
		- `a and b` --> True `if both are` True
		- `a or b` --> True `if either of both are` True
		
		---
		| A | B | A and B | A or B |
		---
		| True | True | True | True |
		| True | False | False | True |
		| False | True | False | True |
		| False | False | False | False |
		---