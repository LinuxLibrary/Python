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
	t[0] 			--> evaluates to 2
	(2,"mit",3) + (5,6)	--> evaluates to(2,"mit",3,5,6)
	t[1:2] 		--> slice tuple, evaluates to ("mit",)
	t[1:3] 		--> slice tuple, evaluates to ("mit",3)
	len(t) 		--> evaluates to 3
	t[1] = 4 		--> gives error, can’t modify object
	```
	
	- Conveniently used to swapvariable values
	
		| Not possible / Error | Using Temp Variable | Using Tuple |
		|:--------------------:|:-------------------:|:-----------:|
		| x = y | temp = x | (x, y) = (y, x)|
		| y = x | x = y | |
		| |y = temp | |
		
	- Used to return more than one value from a function
	
		```
		def quotient_and_remainder(x, y):
			q = x // y
			r = x % y
			return(q, r)
			(quot, rem) = quotient_and_remainder(4,5)
		```
		
- **MANIPULATING TUPLES**
	- Can iterateover tuples
	
	```
	def get_data(aTuple):
		nums= ()
		words = ()
		for t in aTuple:
			nums= nums+ (t[0],)
			if t[1] not in words:
				words = words + (t[1],)
		min_n= min(nums)
		max_n= max(nums)
		unique_words= len(words)
		return (min_n, max_n, unique_words)
	```
	
- **LISTS**
	- Orderedsequenceof information, accessible by index
	- A list is denoted by squarebrackets, []
	- A list contains elements
		- Usually homogeneous (ie, all integers)
		- Can contain mixed types (not common)
	- List elements can be changed so a list is mutable
	
- **INDICES AND ORDERING**
	
	```
	a_list= []
	L = [2, 'a', 4, [1,2]]
	len(L)	--> evaluates to 4
	L[0]	--> evaluates to 2
	L[2]+1	--> evaluates to 5
	L[3] 	--> evaluates to [1,2], another list!
	L[4]	--> gives an error
	i= 2
	L[i-1]	--> evaluates to ‘a’ since L[1]='a' above
	```
	
- **CHANGING ELEMENTS**
	- Lists are mutable!
	- Assigning to an element at an index changes the value
	
	```
	L = [2, 1, 3]
	L[1] = 5
	```
	
	- L is now [2, 5, 3], note this is the same object L
	
- **ITERATING OVER A LIST**
	- compute the sum of elements of a list
	- common pattern, iterate over list elements

	total = 0 | total = 0
	for iin range(len(L)): | for i in L:
		total += L[i] | 	total += i
	print total | print total

	- notice
		- list elements are indexed 0 to len(L)-1
		- range(n)goes from 0 to n-1