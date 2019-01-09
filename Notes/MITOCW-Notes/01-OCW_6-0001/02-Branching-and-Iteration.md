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
		
		| A | B | A and B | A or B |
		|---|---|---------|--------|
		| True | True | True | True |
		| True | False | False | True |
		| False | True | False | True |
		| False | False | False | False |

- **CONTROL FLOW - BRANCHING - `if`**

	```
	if <condition>:
	    <expression>
		<expression>
		...
	```
	
	```
	if <condition>:
		<expression>
		<expression>
		...
	else:
		<expression>
		<expression>
		...
	```
	
	```
	if <condition>:
		<expression>
		<expression>
		...
	elif <condition>:
		<expression>
		<expression>
		...
	else:
		<expression>
		<expression>
		...
	```
	
	- `<condition>` has a value `True` or `False`
	- Evaluate expressions in the block if `<condition>` is `True`
	
	- **INDENTATION**
		- Matters in Python
		- How you denote blocks of code
		
- **CONTROL FLOW: `while` LOOPS**

	```
	while <condition>:
		<expression>
		<expression>
	```
	
	- `<condition>` evaluates to a Boolean
	- If <condition> is True, do all the steps in the code block
	- Check <condition> again
	- repeat until <condition> is False
	- Example program
	
	```
	n = input("You're in the lost forest. Go left or right? ")
	while n == "right":
		n = input("You're in the lost forest. Go left or right? ")
	print("You got out of the lost forest!")
	```
	
	- Iterate through numbers in sequence
	
	```
	n = 0
	while n < 5:
		print(5)
		n = n + 1
	```
	
- **CONTROL FLOW: `for` LOOPS**
	
	```
	for <variable> in range(<some_num>):
		<expression>
		<expression>
		...
	```
	
	- Each time through the loop, <variable> takes a value
	- First time, <variable> starts at a smallest value
	- Next time, <variable> gets the previous value + 1
	
	- **range(start,stop,step)**
		- Default values are `start = 0` and `step = 1` and optional
		- Loop until value is `stop - 1`
		
		```
		mysum = 0
		for i in range(7, 10):
			mysum += 1
		print(mysum)
		
		mysum = 0
		for i in range(5, 11, 2):
			mysum += i
		print(mysum)
		```
		
	- **break STATEMENT**
		- Immediately exits whatever loop it is in
		- Skips remaining expressions in the code block
		- Exits only innermost loop
		
		```
		while <condition_1>:
			while <condition_2>:
				<expression_a>
				break
				<expression_b>
			<expression_c>
		```
		
- **COMPARING `for` and `while` LOOPS**
	| for loops | while loops |
	|-------------|---------------|
	| 1. Know number of iterations | 1. Unbounded number of iterations |
	| 2. Can end early via break | 2. Can end early via break |
	| 3. Uses a counter | 3. Can use a counter but must initialize before loop and increment it inside the loop |
	| 4. Can rewrite a `for` loop using a `while` loop | 4. May not be able to rewrite a `while` loop using a `for` loop |