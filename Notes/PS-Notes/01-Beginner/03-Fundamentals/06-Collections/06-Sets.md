# Set

- Set is an unordered collection of unique and immutable objects

- Creating a Set
	```
	In [2]: p = {6, 28, 12, 9809, 98, 98}
	
	In [3]: p
	Out[3]: {6, 12, 28, 98, 9809}
	```
	
- Creating an empty set

	```
	In [4]: e = set()
	
	In [5]: e
	Out[5]: set()
	```
	
- Converting a list to set

	```
	In [6]: l = [1, 2, 3, 4, 5]
	
	In [7]: s = set(l)
	
	In [8]: s
	Out[8]: {1, 2, 3, 4, 5}
	```
	
- As we know that set is a collection of unique objects, it will remove the duplicates

	```
	In [9]: d = [1, 2, 3, 1, 4, 5, 1, 4, 6, 7]
	
	In [10]: d
	Out[10]: [1, 2, 3, 1, 4, 5, 1, 4, 6, 7]
	
	In [11]: s = set(d)
	
	In [12]: s
	Out[12]: {1, 2, 3, 4, 5, 6, 7}
	```
	
- Adding an element to a set

	```
	In [14]: k = {12, 48}
	
	In [15]: k.add(56)
	
	In [16]: k
	Out[16]: {12, 48, 56}
	```
	
- Adding multiple values to a set

	```
	In [17]: k.update([23, 34, 45])
	
	In [18]: k
	Out[18]: {12, 23, 34, 45, 48, 56}
	```
	
- Removing an element from a set
	- For removing element we can use `remove` or `discard`
	- `remove` will give a KeyError if the element is not present in the set
	- `discard` will succeed even if the element is not present as well.
	
	```
	In [19]: k.remove(11)
	---------------------------------------------------------------------------
	KeyError                                  Traceback (most recent call last)
	<ipython-input-19-0e38e7c2ce90> in <module>()
	----> 1 k.remove(11)
	
	KeyError: 11
	
	In [20]: k.discard(11)
	```
	
- 