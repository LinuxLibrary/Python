# Collection protocols

- Container
	- Applicable on `str, list, range, tuple, bytes, set, dict`
	- Membership testing using `in` and `not in`
	
- Sized
	- Applicable on `str, list, range, tuple, bytes, set, dict`
	- Determine number of elements with `len()`
	
- Iterable
	- Applicable on `str, list, range, tuple, bytes, set, dict`
	- Can produce an iterator with iter()
	
	```
	for item in iterable:
		do_something(item)
	```
	
- Sequence
	- Applicable on `str, list, range, tuple, bytes`
	- Retrieve elements by index
	
		```
		item = seq[index]
		```
		
	- Find items by value
	
		```
		index = seq.index(item)
		```
		
	- Count items
	
		```
		num = seq.count(item)
		```
		
	- Produce a reversed sequence
	
		```
		r = reversed(seq)
		```