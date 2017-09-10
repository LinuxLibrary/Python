# Conditional Statements in Python

* ***`if` statement***
	- In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Conditional statements give us this ability. The simplest form is the if statement, which has the genaral form:
	
	```
	if BOOLEAN EXPRESSION:
		STATEMENTS
	```

	- A few important things to note about if statements:
		- The colon (:) is significant and required. It separates the header of the compound statement from the body.
		- The line after the colon must be indented. It is standard in Python to use four spaces for indenting.
		- All lines indented the same amount after the colon will be executed whenever the BOOLEAN_EXPRESSION is true.

* ***`if else` statement***
	- It is frequently the case that you want one thing to happen when a condition it true, and something else to happen when it is false. For that we have the if else statement.

	```
	if food == 'spam':
		print('Ummmm, my favorite!')
	else:
		print("No, I won't have it. I want spam!")
	```

	- Here, the first print statement will execute if food is equal to 'spam', and the print statement indented under the else clause will get executed when it is not.

* ***Chained Conditionals***
	- Sometimes there are more than two possibilities and we need more than two branches. One way to express a computation like that is a chained conditional:

	```
	if x < y:
		STATEMENTS_A
	elif x > y:
		STATEMENTS_B
	else:
		STATEMENTS_C
	```

	- `elif` is an abbreviation of `else if`. Again, exactly one branch will be executed. There is no limit of the number of elif statements but only a single (and optional) final else statement is allowed and it must be the last branch in the statement.

* ***Nested Conditionals***
	- One conditional can also be nested within another. (It is the same theme of composibility, again!) We could have written the previous example as follows:

	```
	if x < y:
		STATEMENTS_A
	else:
		if x > y:
			STATEMENTS_B
		else:
			STATEMENTS_C
	```

	- The outer conditional contains two branches. The second branch contains another if statement, which has two branches of its own. Those two branches could contain conditional statements as well.
	- Although the indentation of the statements makes the structure apparent, nested conditionals very quickly become difficult to read. In general, it is a good idea to avoid them when you can.
	- Logical operators often provide a way to simplify nested conditional statements. For example, we can rewrite the following code using a single conditional:

	```
	if 0 < x:            # assume x is an int here
		if x < 10:
			print("x is a positive single digit.")
	```

	- The print function is called only if we make it past both the conditionals, so we can use the and operator:
	
	```
	if 0 < x and x < 10:
		print("x is a positive single digit.")
	```
	
	- Python actually allows a short hand form for this, so the following will also work:
	
	```
	if 0 < x < 10:
		print("x is a positive single digit.")
	```
