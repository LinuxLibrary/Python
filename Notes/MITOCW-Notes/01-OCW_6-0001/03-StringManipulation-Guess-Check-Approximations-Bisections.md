# String Manipulation, Guess and Check, Approximations, Bisection

- **STRINGS**
	- Think of as a sequence of case sensitive characters
	- Can compare strings with `==`, `>`, `<` etc.
	- `len()` is a function used to retrieve the length of the string in the parentheses
	
	```
	>>> s = "abc"
	>>> len(s) --> evalutes to 3
	```
	
	- Square brackets used to perform indexing into a string to get the value at a certain index/position
	- Indexing starts at `0`
	- Last character always starts at index `-1`
	
	```
	>>> s = "abc"
	>>> s[0]	--> evalutes to "a"
	>>> s[1]	--> evalutes to "b"
	>>> s[2]	--> evalutes to "c"
	>>> s[3]	--> trying to index out of bounds, error
	>>> s[-1]	--> evalutes to "c"
	>>> s[-2]	--> evalutes to "b"
	>>> s[-3]	--> evalutes to "a"
	```
	
	- Can slice strings using `[start:stop:step]`
	- If we give two numbers, `[start:stop]`, `step=1` by default
	- You can also omit numbers and leave just colons
	
	```
	>>> s = "abcdefgh"
	>>> s[3:6] --> evalutes to "def", same as s[3:6:1]
	>>> s[3:6:2] --> evalutes to "df"
	>>> s[::] --> evalutes to "abcdefgh", same as s[0:len(s):1]
	>>> s[::-1] --> evalutes to "hgfedcba", same as s[-1:-(len(s)+1):-1]
	>>> s[4:1:-2] --> evalutes to "ec"
	```
	
	- Strings are **immutable** - cannot be modified
	
	```
	>>> s = "hello"
	>>> s[0] = 'y' --> gives an error
	>>> s = 'y'+s[1:len(s)] --> is allowed, s bound to new object
	```
	
- **STRINGS AND LOOPS**
	- These two code snippets do the same thing
	- Bottom one is more **pythonic**
	
	```
	>>> s = "abcdefgh"
	>>> for index in range(len(s)):
	... 	if s[index] == 'i' or s[index] == 'u':
	... 		print("There is an i or u")
	
	>>> for char in s:
	... 	if char == 'i' or char == 'u':
	... 		print("There is an i or u")
	```
	
	- Sample code
	
	```
	>>> an_letters = "aefhilmnorsxAEFHILMNORSX"
	>>> word = input("I will cheer for you! Enter a word: ")
	>>> times = int(input("Enthusiasm level (1-10): "))
	
	>>> i = 0
	>>> while i < len(word):
	... 	char = word[i]
	... 	if char in an_letters:
	... 		print("Give me an " + char + "! " + char)
	... 	else:
	... 		print("Give me a " + char + "! " + char)
	... 	i += 1
	... print("What does that spell?")
	... for i in range(times):
	... 	print(word, "!!!")
	```
	
	- Rewriting the same code using `for` loop
	
	```
	>>> an_letters = "aefhilmnorsxAEFHILMNORSX"
	>>> word = input("I will cheer for you! Enter a word: ")
	>>> times = int(input("Enthusiasm level (1-10): "))
	
	>>> for char in word:
	... 	if char in an_letters:
	... 		print("Give me an " + char + "! " + char)
	... 	else:
	... 		print("Give me a " + char + "! " + char)
	... print("What does that spell?")
	... for i in range(times):
	... 	print(word, "!!!")
	```
	
- **ALGORITHMS**
	- **GUESS-AND-CHECK - cube root**

		```
		cube = 8
		for guess in range(abs(cube)+1):
			if guess**3 >= abs(cube):
				break
			if guess**3 != abs(cube):
				print(cube, "is not a perfect cube!")
			else:
				if cube < 0:
					guess = -guess
				print('Cube root of ' + str(cube) + ' is ' + str(guess))
		```
	
	- **APPROXIMATE SOLUTIONS**
		- Good enough solution
		- Start with a guess and increment by some small value
		- Keep guessing if `|guess^{3}-cube| >= epsilon` for some small epsilon
		- Decreasing increment size --> slower program
		- Increasing esilon --> less accurate answer