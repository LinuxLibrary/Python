# Lists in Python

- The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.
- Creating a list is as simple as putting different comma-separated values between square brackets.

```
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
```

- Similar to string indices, list indices start at 0, and lists can be sliced, concatenated and so on.

- ***Accessing Values in Lists***
	- To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that index.

	```
	list1 = ['physics', 'chemistry', 1997, 2000];
	list2 = [1, 2, 3, 4, 5, 6, 7 ];

	print list1
	['physics', 'chemistry', 1997, 2000]

	print list1[1:]
	['chemistry', 1997, 2000]

	print list1[2:]
	[1997, 2000]

	print list1[3:]
	[2000]

	print list1[0:len(list1)]
	['physics', 'chemistry', 1997, 2000]

	print list1[0:len(list1)-1]
	['physics', 'chemistry', 1997]
	```

- ***Updating Lists***
	- You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator, and you can add to elements in a list with the append() method.
	
	```
	list = ['physics', 'chemistry', 1997, 2000]

	print "Value available at index 2 : "
	print list[2]
	list[2] = 2001
	print "New value available at index 2 : "
	print list[2]
	```

	- Output:

	```
	Value available at index 2 :
	997
	ew value available at index 2 :
	2001
	```
	
- ***Delete List Elements***
	- To remove a list element, you can use either the del statement if you know exactly which element(s) you are deleting or the remove() method if you do not know.
	
	```
	list1 = ['physics', 'chemistry', 1997, 2000]

	print list1
	del list1[2]
	print "After deleting value at index 2 : "
	print list1
	```

	- Output:

	```
	['physics', 'chemistry', 1997, 2000]
	After deleting value at index 2 :
	['physics', 'chemistry', 2000]
	```

- ***Built-in List Functions & Methods***

SN | Function | Description
---|----------|--------------
1 | cmp(list1, list2) | Compares elements of both lists.
2 | len(list) | Gives the total length of the list.
3 | max(list) | Returns item from the list with max value.
4 | min(list) | Returns item from the list with min value.
5 | list(seq) | Converts a tuple into list.

- Python includes following list methods

SN | Function | Description
---|----------|--------------
1 | list.append(obj) | Appends object obj to list
2 | list.count(obj) | Returns count of how many times obj occurs in list
3 | list.extend(seq) | Appends the contents of seq to list
4 | list.index(obj) | Returns the lowest index in list that obj appears
5 | list.insert(index, obj) | Inserts object obj into list at offset index
6 | list.pop(obj=list[-1]) | Removes and returns last object or obj from list
7 | list.remove(obj) | Removes object obj from list
8 | list.reverse() | Reverses objects of list in place
9 | list.sort([func]) | Sorts objects of list, use compare func if given
