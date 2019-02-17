# Recursion, Dictionaries

- **RECURSION**
	- Recursion is the process of repeating items in a self-similar way.
	- **Algorithmically:** a way to design solutions to problems by divide-and-conquer or decrease-and-conquer
		- Reduce a problem to simpler versions of the same problem
	- **Semantically:** a programming technique where a function calls itself
		- In programming, goal is to NOT have infinite recursion
			- Must have 1 or more base cases that are easy to solve
			- Must solve the same problem on some other input with the goal of simplifying the larger problem input
	
	- **ITERATIVE ALGORITHMS SO FAR**
		- Looping constructs (while and for loops) lead to iterative algorithms 
		- Can capture computation in a set of state variables that update on each iteration through loop
		
	- **MULTIPLICATION – ITERATIVE SOLUTION**
		- “multiply a * b” is equivalent to “add a to itself b times”
		- Capture state by 
			- An iteration number (i) starts at b
				`i <- i-1 and stop when 0`
			- A current value of computation (result)
				`result <- result + a`
				
			```
			def mult_iter(a, b):
				result = 0
				while b > 0: 
					result += a
					b -= 1
				return result
			```
			
	- **MULTIPLICATION – RECURSIVE SOLUTION**
		- Recursive step
			- Think how to reduce problem to a simpler/smaller version of same problem
		- Base case 
			- Keep reducing problem until reach a simple case that can be solved directly
			- When b = 1, a*b = a
			
	- **FACTORIAL**
		- `n! = n*(n-1)*(n-2)*(n-3)* … * 1`
		- For what n do we know the factorial?
		- n = 1
		
			```
			if n == 1:
				return 1
			```
		
		- How to reduce problem? Rewrite in terms of something simpler to reach base case
		- n*(n-1)!
		
			```
			else:
				return n*factorial(n-1)
			```
		
		```
		def factorial(n):
			if n == 1:
				return 1
			else:
				return n*factorial(n-1)
		```
		
		- Each recursive call to a function creates its own scope/environment
		- Bindings of variables in a scope are not changed by recursive call
		- Flow of control passes back to previous scope once funcSon call returns value
		
	- **ITERATIONvs. RECURSION**
		- Iteration
		
		```
		def factorial_iter(n):
			prod = 1
			for i in range(1,n+1):
				prod *= i
			return prod
		```
		
		- Recursion
		
		```
		def factorial(n):
			if n == 1:
				return 1
			else:
				return n*factorial(n-1)
		```
		
		- Recursion may be simpler, more intuitive
		- Recursion may be efficient from programmer Point Of View
		- Recursion may not be efficient from computer Point Of View
		
	- **INDUCTIVE REASONING**
		- How do we know that our recursive code will work?
		- mult_iter terminates because b is iniSally positive, aand decreases by 1 each time around loop; thus must eventually become less than 1
		
		```
		def mult_iter(a, b):
			result = 0
			while b > 0:
				result += a
				b -= 1
			return result
		```
		
		- mult called with b = 1 has no recursive call and stops
		- mult called with b > 1 makes a recursive call with a smaller version of b; must eventually reach call with b = 1
		
		```
		def mult(a, b):
			if b == 1:
				return a
			else:
				return a + mult(a, b-1)
		```
		
	- **MATHEMATICAL INDUCTION**
		- To prove a statement indexed on integers is true for all values of n:
			- Prove it is true when n is smallest value (e.g. n = 0 or n = 1)
			- Then prove that if it is true for an arbitrary value of n, one can show that it must be true for n+1
			
	- **EXAMPLE OF INDUCTION**
		- 0 + 1 + 2 + 3 + … + n = (n(n+1))/2
		- Proof:
			- If n = 0, then LHS is 0 and RHS is 0*1/2 = 0, so true
			- Assume true for some k, then need to show that
				- `0 + 1 + 2 + … + k + (k+1) = ((k+1)(k+2))/2`
				- LHS is k(k+1)/2 + (k+1) by assumpSon that property holds for problem of size k
				- This becomes, by algebra, ((k+1)(k+2))/2
			- Hence expression holds for all n >= 0
			
	- **RELEVANCE TO CODE?**
		- Same logic applies
		
		```
		def mult(a, b):
			if b == 1:
				return a
			else:
				return a + mult(a, b-1)
		```
		
		- Base case, we can show that mult must return correct answer
		- For recursive case, we can assume that mult correctly returns an answer for problems of size smaller than b, then by the addiSon step, it must also return a correct answer for problem of size b
		- Thus by inducSon, code correctly returns answer
		
	 - **TOWERS OF HANOI**
		- The story:
			- 3 tall spikes
			- Stack of 64 different sized discs – start on one spike
			- Need to move stack to second spike (at which pointuniverse ends)
			- Can only move one disc at a time, and a larger disc can never cover up a small disc
			- Having seen a set of examples of different sized stacks, how would you write a program to print out the right set of moves?
			- Think recursively!
				- Solve a smaller problem 
				- Solve a basic problem 
				- Solve a smaller problem
			
			```
			def printMove(fr, to):
				print('move from ' + str(fr) + ' to ' + str(to))
				
			def Towers(n, fr, to, spare):
				if n == 1:
					printMove(fr, to)
				else:
					Towers(n-1, fr, spare, to)
					Towers(1, fr, to, spare)
					Towers(n-1, spare, to, fr)
			```
			
	- **RECURSION WITH MULTIPLE BASE CASES**
		- Fibonacci numbers
			- Leonardo of Pisa (aka Fibonacci) modeled the following challenge
				- Newborn pair of rabbits (one female, one male) are put in a pen
				- Rabbits mate at age of one month 
				- Rabbits have a one month gestation period 
				- Assume rabbits never die, that female always produces one new pair (one male, one female) every month from its second month on. 
				- How many female rabbits are there at the end of one year?
			- **FIBONACCI**
				- After one month (call it 0) – 1 female 
				- After second month – still 1 female (now pregnant)
				- After third month – two females, one pregnant, one not
				- In general, females(n) = females(n-1) + females(n-2) 
				- Every female alive at month n-2 will produce one female in month n; 
				- These can be added those alive in month n-1 to get total alive in month n
				- Base cases: 
					- Females(0) = 1 
					- Females(1) = 1
				- Recursive case 
					- Females(n) = Females(n-1) + Females(n-2)
					
				```
				def fib(x):
					"""assumes x an int >= 0returns Fibonacci of x"""
					if x == 0 or x == 1:
						return 1
					else:
						return fib(x-1) + fib(x-2)
				```
				
		- **RECURSION ON NON-NUMERICS**
			- How to check if a string of characters is a palindrome, i.e.,reads the same forwards and backwards
				- “Able was I, ere I saw Elba” – avributed to Napoleon 
				- “Are we not drawn onward, we few, drawn onward to new era?” – avributed to Anne Michaels
			- **SOLVING RECURSIVELY?**
				- First, convert the string to just characters, by stripping out punctuation, and converting upper case to lower case
				- Then
					- Base case: a string of length 0 or 1 is a palindrome 
					- Recursive case:
						- If first character matches last character, then is a palindrome if middle section is a palindrome
			- **EXAMPLE**
				- ‘Able was I, ere I saw Elba’ à ‘ablewasiereisawleba’
				- isPalindrome(‘ablewasiereisawleba’) is same as
					- ‘a’ == ‘a’ and isPalindrome(‘blewasiereisawleb’)
					
				```
				def isPalindrome(s):
					
					def toChars(s):
						s = s.lower()
						ans = ''
						for c in s:
							if c in 'abcdefghijklmnopqrstuvwxyz':
								ans = ans + c
						return ans
					
					def isPal(s):
						if len(s) <= 1:
							return True
						else:
							return s[0] == s[-1] and isPal(s[1:-1])
					
					return isPal(toChars(s))
				```
				
		- **DIVIDE AND CONQUER**
			- An example of a “divide and conquer” algorithm
			- Solve a hard problem by breaking it into a set of sub-problems such that:
				- Sub-problems are easier to solve than the original
				- Solutions of the sub-problems can be combined to solve the original

- **DICTIONARIES**
	- So far, can store using separate lists for every info
	
	```
	names = ['Ana', 'John', 'Denise', 'Katy']
	grade = ['B', 'A+', 'A', 'A']
	course = [2.00, 6.0001, 20.002, 9.01]
	```
	
	- A separate list for each item
	- Each list must have the same length
	- Info stored across lists at same index, each index refers to info for a different person
	
	- **HOW TO UPDATE/RETRIEVE STUDENT INFO**
		
		```
		def get_grade(student, name_list, grade_list, course_list):
			i = name_list.index(student)
			grade = grade_list[i]
			course = course_list[i]
			return (course, grade)
		```
		
		- Messy if have a lot of different info to keep track of
		- Must maintain many lists and pass them as arguments
		- Must always index using integers
		- Must remember to change mulSple lists
		
	- **A BETTER AND CLEANER WAY – A DICTIONARY**
		- Nice to index item of interest directly (not always int)
		- Nice to use one data structure, no separate lists
			- List:

			| Index | Element |
			|-------|---------|
			| 0 | Elem 1 |
			| 1 | Elem 2 |
			| 2 | Elem 3 |
			| ... | ... |
			
			- Dictionary:
			
			| Key | Value |
			|-----|-------|
			| Key 1 | Val 1 |
			| Key 2 | Val 2 |
			| Key 3 | Val 3 |
			| Key 4 | Val 4 |
			| ... | ... |
			
	- **A PYTHON DICTIONARY**
		- Store pairs of data 
			- Key
			- Value
			
		```
		my_dict = {}
		grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
		```
		
	- **DICTIONARY LOOKUP**
		- Similar to indexing into a list
		- Looks up the key
		- Returns the value associated with the key 'A'
		- If key isn’t found, get an error
		
		```
		grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
		grades['John'] à evaluates to 'A+'
		grades['Sylvan'] à gives a KeyError
		```
		
	- **DICTIONARY OPERATIONS**
		- `grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}`
		- Add an entry 
			- `grades['Sylvan'] = 'A'`
		- Test if key in dictionary
			- 'John' in gradesàreturns True
			- 'Daniel' in gradesàreturns False
		- Delete entry 
			- `del(grades['Ana'])`
		- Get an iterable that acts like a tuple of all keys
			- `grades.keys() -> returns ['Denise','Katy','John','Ana']`
			
			> NOTE: No guaranteed order
			
		- Get an iterable that acts like a tuple of all values
			- `grades.values() -> returns ['A', 'A', 'A+', 'B']`
			
			> NOTE: No guaranteed order
			
	- **DICTIONARY KEYS and VALUES**
		- Values
			- Any type (immutable and mutable)
			- Can be duplicates
			- Dictionary values can be lists, even other dictionaries!
		- Keys
			- Must be unique
			- Immutable type (int, float, string, tuple,bool)
				- Actually need an object that is hashable, but think of as immutable as all immutable types are hashable
			- Careful with float type as a key
		- No order to keys or values!
			- `d = {4:{1:0}, (1,3):"twelve", 'const':[3.14,2.7,8.44]}`
			
	- **LIST vs DICTIONARY**
	
		|:list:|:dict:|
		|------|------|
		| - Ordered sequence of elements | - Matches "Keys" to "Values" |
		| - Lookup elements by an integer index | - look up one item by another item |
		| - Indices have an order | - No order is guaranteed |
		| - Index is an integer | - Key can be any immutable type |
		
	- 