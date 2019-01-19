# Decomposition, Abstraction, Functions

- **CREATE STRUCTURE with DECOMPOSITION**
	- In programming, divide code into modules
		- Are self-contained
		- Used to break upcode
		- Intended to be reusable
		- Keep code organized
		- Keep code coherent
		
- **SUPRESS DETAILS with ABSTRACTION**
	- In programming, think of a piece of code as a black box
		- Cannot see details
		- Do not need to see details
		- Do not want to see details
		- Hide tedious coding details
	- Achieve abstraction with function specificationsor docstrings

- **FUNCTIONS**
	- Write reusable pieces/chunks of code, called functions
	- Functions are not run in a program until they are “called” or “invoked” in a program
	- Function characteristics:
		- Has a name
		- Has parameters(0 or more)
		- Has a docstring(optional but recommended)
		- Has a body
		- Returns something
		
- **HOW TO WRITE and CALL/INVOKE A FUNCTION**

	```
	def is_even( i):
		"""
		Input: i, a positive int
		Returns True if iis even, otherwise False
		"""
		print("inside is_even")
		return i%2 == 0
	```

	```
	is_even(3)
	```
	
- **VARIABLE SCOPE**
	- Formal parameter gets bound to the value of actual parameter when function is called
	- New scope/frame/environmentcreated when enter a function
	- Scope is mapping of names to objects
	
	```
	def f( x ):
		x = x + 1
		print('in f(x): x =', x)
		return x
	```
	
	```
	x = 3
	z = f( x )
	```
	
- **ONE WARNING IF NO returnSTATEMENT**
	
	```
	def is_even( i):
		"""
		Input: i, a positive int
		Does not return anything
		"""
		i%2 == 0
	```
	
	- Python returns the value None, if no returngiven
	- Represents the absence of a value

- **SAMPLE PROGRAMS**
	- [Functions](https://github.com/LinuxLibrary/Python/blob/master/Programs/MITOCW/01-OCW_6-0001/lec4_functions.py)
	
- **return vs. print**
	| Return | Print |
	|--------|-------|
	| Return only has meaning insidea function | Print can be used outsidefunctions |
	| Only one return executed inside a function | Can execute many print statements inside a function |
	| Code inside function but after return statement not executed | Code inside function can be executed after a print statement |
	| Has a value associated with it, given to function caller | Has a value associated with it, outputtedto the console |