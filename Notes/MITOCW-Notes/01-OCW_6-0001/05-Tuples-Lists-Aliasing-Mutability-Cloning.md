# Tuples, Lists, Aliasing, Mutability, Cloning

- **Compound Data Types**
	- The 2 compound data types are
		- Tuples
		- Lists
	- Idea of aliasing
	- Idea of mutability
	- Idea of cloning
	
- **TUPLES**
	- An ordered sequence of elements, can mix element types
	- Cannot change element values, immutable
	- Represented with parentheses
	
	```
	te= ()
	t = (2,"mit",3)
	t[0] 				--> evaluates to 2
	(2,"mit",3) + (5,6)	--> evaluates to(2,"mit",3,5,6)
	t[1:2] 				--> slice tuple, evaluates to ("mit",)
	t[1:3] 				--> slice tuple, evaluates to ("mit",3)
	len(t) 				--> evaluates to 3
	t[1] = 4 			--> gives error, can’t modify object
	```
	
	- Conveniently used to swapvariable values
	
		Not possible / Error | Using Temp Variable | Using Tuple
		x = y | temp = x | (x, y) = (y, x)
		y = x | x = y | 
		|y = temp | 
		
	- Used to return more than one value from a function
	
		```
		def quotient_and_remainder(x, y):
			q = x // y
			r = x % y
			return(q, r)
			(quot, rem) = quotient_and_remainder(4,5)
		```
		