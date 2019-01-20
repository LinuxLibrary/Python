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
	- Compute the sum of elements of a list
	- Common pattern, iterate over list elements

	```
	total = 0
	for i in range(len(L)):
		total += L[i]
	print total
	```
	
	```
	total = 0
	for i in L:
		total += i
	print total
	```

	- Notice
		- List elements are indexed 0 to len(L)-1
		- Range(n)goes from 0 to n-1
		
- **OPERATIONS ON LISTS -ADD**
	- Add elements to end of list with L.append(element)
	- Mutates the list!
	
	```
	L = [2,1,3]
	L.append(5)	--> L is now [2,1,3,5]
	```
	
	- What is the dot?
		- Lists are Python objects, everything in Python is an object
		- Objects have data
		- Objects have methods and functions
		- Access this information by object_name.do_something()
	- To combine lists together use concatenation, + operator, to give you a new list
	- Mutate list with L.extend(some_list)
	
	```
	L1 = [2,1,3]
	L2 = [4,5,6]
	L3 = L1 + L2	--> L3 is [2,1,3,4,5,6]L1, L2 unchanged
	L1.extend([0,6])	--> mutated L1to [2,1,3,0,6]
	```
	
- **OPERATIONS ON LISTS -REMOVE**
	- Delete element at a specific index withdel(L[index])
	- Remove element at end of list with L.pop(), returns the removed element
	- Remove a specific element with L.remove(element)
		- Looks for the element and removes it
		- If element occurs multiple times, removes first occurrence
		- If element not in list, gives an error
		
		```
		L = [2,1,3,6,3,7,0] # do below in order
		L.remove(2)	--> mutates L = [1,3,6,3,7,0]
		L.remove(3)	--> mutates L = [1,6,3,7,0]
		del(L[1]) 	--> mutates L = [1,3,7,0]
		L.pop()	--> returns 0 and mutates L = [1,3,7]
		```
		
- **CONVERT LISTS TO STRINGS AND BACK**
	- Convert string to list with list(s), returns a list with every character from san element in L
	- Can use s.split(), to split a string on a character parameter, splits on spaces if called without a parameter
	- Use ''.join(L) to turn a list of characters into a string, can give a character in quotes to add char between every element
	
	```
	s = "I<3 cs"	--> sis a string
	list(s) 	--> returns ['I','<','3',' ','c','s']
	s.split('<') 	--> returns ['I', '3 cs']
	L = ['a','b','c']	--> Lis a list
	''.join(L)	--> returns "abc"
	'_'.join(L)	--> returns "a_b_c"
	```
	
- **OTHER LIST OPERATIONS**
	- sort() and sorted()
	- reverse()
	- And many more ...
	
	```
	L=[9,6,0,3]
	sorted(L)	--> returns sorted list, does not mutateL
	L.sort()	--> mutatesL=[0,3,6,9]
	L.reverse()	--> mutatesL=[9,6,3,0]
	```
	
- **LISTS IN MEMORY**
	- Lists are mutable
	- Behave differently than immutable types
	- Is an object in memory
	- Variable name points to object
	- Any variable pointing to that object is affected
	- Key phrase to keep in mind when working with lists is side effects
	
- **CLONING A LIST**
	- Create a new list and copy every element using
	
	```
	chill = cool[:]
	```
	
- **SORTING LISTS**
	- Calling sort() mutates the list, returns nothing
	- Calling sorted() does not mutate list, must assign result to a variable
	
- **LISTS OF LISTS OF LISTS OF...**
	- Can have nestedlists
	- Side effects still possible after mutation
	
- **MUTATION AND ITERATION**
	- Avoid mutating a list as you are iterating over it
	- Wrong method
	
	```
	def remove_dups(L1, L2):
		for e in L1:
			if e in L2:
				L1.remove(e)
	```
	
	- Correct method
	
	```
	defremove_dups(L1, L2):
		L1_copy = L1[:]
		for e in L1_copy:
			if e in L2:
				L1.remove(e)
	```
	
	```
	L1 = [1, 2, 3, 4]
	L2 = [1, 2, 5, 6]
	remove_dups(L1, L2)
	```
	
	- L1 is [2,3,4] not [3,4] Why?
		- Python uses an internal counter to keep track of index it is in the loop
		- Mutating changes the list length but Python doesn’t update the counter
		- Loop never sees element 2