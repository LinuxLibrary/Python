# Exceptions

- Raise an exception to interrupt the program flow.
- Handle an exception to resume control.
- Unhandled exceptions will terminate the program.
- Exception objects contain information about the exceptional event.
- Exceptions can be handled using the `try`, `except` blocks.
- The code we want to execute can be declared in the `try` block and the error handling actions can be written in the `except` block.
- While writting code in the `except` block we can define those for a specific error or else for anytype of error.
	- For specific error
	
	```
	except ValueError:
		print("Encountered ValueError")
	```
	
	- In this method the error message can be printed as follows:
	
	```
	except IOError as e:
		print("Unable to open file!\nError:" + str(e))
	```
	
	- For any error that we are not sure of
	
	```
	except:
		print("Error!")
	```
	
	- In this method the error message can be printed as follows:
	
	```
	except Exception as e:
		print("Unable to open file!\nError:" + str(e))
	```