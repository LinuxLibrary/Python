# Loops (or) Iteration in Python

- Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that computers do well and people do poorly.
- Repeated execution of a set of statements is called iteration. Python has two statements for iteration – the for statement, which we met last chapter, and the while statement.

* ***`for` loop***
	- The for loop processes each item in a sequence, so it is used with Python’s sequence data types - strings, lists, and tuples.
	- Each item in turn is (re-)assigned to the loop variable, and the body of the loop is executed.
	- The general form of a for loop is:

	```
	for LOOP_VARIABLE in SEQUENCE:
		STATEMENTS
	```

	- This is another example of a compound statement in Python, and like the branching statements, it has a header terminated by a colon (:) and a body consisting of a sequence of one or more statements indented the same amount from the header.
	- The loop variable is created when the for statement runs, so you do not need to create the variable before then. Each iteration assigns the the loop variable to the next element in the sequence, and then executes the statements in the body. The statement finishes when the last element in the sequence is reached.
	- This type of flow is called a loop because it loops back around to the top after each iteration.

	```
	for friend in ['Margot', 'Kathryn', 'Prisila']:
		invitation = "Hi " + friend + ".  Please come to my party on Saturday!"
		print(invitation)
	```

	- Output:

	```
	Hi Margot. Please come to my party on Satruday!
	Hi Kathryn. Please come to my party on Satruday!
	Hi Prisila. Please come to my party on Satruday!
	```

* ***`while` statement***
	- The general syntax for the while statement looks like this:

	```
	while BOOLEAN_EXPRESSION:
		STATEMENTS
	```

	- Like the branching statements and the for loop, the while statement is a compound statement consisting of a header and a body. A while loop executes an unknown number of times, as long at the BOOLEAN EXPRESSION is true.
	- Here is a simple example:

	```
	number = 0
	prompt = "What is the meaning of life, the universe, and everything? "

	while number != "42":
		number =  input(prompt)
	```

	- Notice that if number is set to 42 on the first line, the body of the while statement will not execute at all.

* ***Choosing between `for` and `while`***
	- Use a for loop if you know, before you start looping, the maximum number of times that you’ll need to execute the body. For example, if you’re traversing a list of elements, you know that the maximum number of loop iterations you can possibly need is “all the elements in the list”.
	- By contrast, if you are required to repeat some computation until some condition is met, and you cannot calculate in advance when this will happen, you’ll need a while loop.
	- We call the first case definite iteration — we have some definite bounds for what is needed. The latter case is called indefinite iteration — we’re not sure how many iterations we’ll need — we cannot even establish an upper bound!

* ***`break` statement***
	- The break statement is used to immediately leave the body of its loop. The next statement to be executed is the first one after the body:

	```
	for i in [12, 16, 17, 24, 29]:
		if i % 2 == 1:  # if the number is odd
			break        # immediately exit the loop
		print(i)
	print("done")
	```

	- Output:

	```
	12
	16
	done
	```

* ***`continue` statement***
	- This is a control flow statement that causes the program to immediately skip the processing of the rest of the body of the loop, for the current iteration. But the loop still carries on running for its remaining iterations:

	```
	for i in range(11):
		if i % 2 == 1:
			continue
		print i
	print "Done"
	```

	- Output:

	```
	2
	4
	6
	8
	10
	```
