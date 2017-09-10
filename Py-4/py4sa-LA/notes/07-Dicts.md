# Python Dictionaries

- Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair.
- Dictionaries are optimized to retrieve values when the key is known.
- An item has a key and the corresponding value expressed as a pair, key: value.
- Dictionaries can be contained in lists and vice versa. But what's the difference between lists and dictionaries? Lists are ordered sets of objects, whereas dictionaries are unordered sets. But the main difference is that items in dictionaries are accessed via keys and not via their position. A dictionary is an associative array (also known as hashes). Any key of the dictionary is associated (or mapped) to a value. The values of a dictionary can be any Python data type. So dictionaries are unordered key-value-pairs. 
- Dictionaries don't support the sequence operation of the sequence data types like strings, tuples and lists. Dictionaries belong to the built-in mapping type. They are the sole representative of this kind!
- Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

## How to create a dictionary?

```
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
```

## Accessing Values in Dictionary
- To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.

	```
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

	print "dict['Name']: ", dict['Name']
	print "dict['Age']: ", dict['Age']
	```

	- Output:
	
	```
	dict['Name']:  Zara
	dict['Age']:  7
	```

## Updating Dictionary
- You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry.

	```
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

	dict['Age'] = 8; # update existing entry
	dict['School'] = "DPS School"; # Add new entry


	print "dict['Age']: ", dict['Age']
	print "dict['School']: ", dict['School']
	```

	- Output:

	```
	dict['Age']:  8
	dict['School']:  DPS School
	```

## Delete Dictionary Elements
- You can either remove individual dictionary elements or clear the entire contents of a dictionary. You can also delete entire dictionary in a single operation.
- To explicitly remove an entire dictionary, just use the del statement.

	```
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

	del dict['Name']; # remove entry with key 'Name'
	dict.clear();     # remove all entries in dict
	del dict ;        # delete entire dictionary

	print "dict['Age']: ", dict['Age']
	print "dict['School']: ", dict['School']
	```

	- This produces the following result. Note that an exception is raised because after del dict dictionary does not exist any more −

	```
	dict['Age']:
	Traceback (most recent call last):
	  File "test.py", line 8, in <module>
	    print "dict['Age']: ", dict['Age'];
	TypeError: 'type' object is unsubscriptable
	```

## How to access elements from a dictionary?
- While indexing is used with other container types to access values, dictionary uses keys. Key can be used either inside square brackets or with the get() method.
- The difference while using get() is that it returns None instead of KeyError, if the key is not found.

	```
	my_dict = {'name':'Jack', 'age': 26}

	# Output: Jack
	print(my_dict['name'])

	# Output: 26
	print(my_dict.get('age'))

	# Trying to access keys which doesn't exist throws error
	# my_dict.get('address')
	# my_dict['address']
	```

- To handle the exception manually we need to give the error message along with the key we are searching for.

	```
	my_dict.get('address','Unable to find address')
	```

## -- Built-in Dictionary Functions & Methods --

SN | Function | Description
---|----------|------------
1 | cmp(dict1, dict2) | Compares elements of both dict.
2 | len(dict) | Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
3 | str(dict) | Produces a printable string representation of a dictionary
4 | type(variable) | Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.

SN | Function | Description
---|----------|------------
1 | dict.clear() | Removes all elements of dictionary dict
2 | dict.copy() | Returns a shallow copy of dictionary dict
3 | dict.fromkeys() | Create a new dictionary with keys from seq and values set to value.
4 | dict.get(key, default=None) | For key key, returns value or default if key not in dictionary
5 | dict.has_key(key) | Returns true if key in dictionary dict, false otherwise
6 | dict.items() | Returns a list of dict's (key, value) tuple pairs
7 | dict.keys() | Returns list of dictionary dict's keys
8 | dict.setdefault(key, default=None) | Similar to get(), but will set dict[key]=default if key is not already in dict
9 | dict.update(dict2) | Adds dictionary dict2's key-values pairs to dict
10 | dict.values() | Returns list of dictionary dict's values
