# Dictionaries

- Like lists dictionaries can easily be changed, can be shrunk and grown ad libitum at run time.
- They shrink and grow without the necessity of making copies.
- Dictionaries can be contained in lists and vice versa.
- But what's the difference between lists and dictionaries? Lists are ordered sets of objects, whereas dictionaries are unordered sets.
- But the main difference is that items in dictionaries are accessed via keys and not via their position.
- A dictionary is an associative array (also known as hashes).
- Any key of the dictionary is associated (or mapped) to a value.
- The values of a dictionary can be any Python data type.
- So dictionaries are unordered key-value-pairs. 
- Dictionaries don't support the sequence operation of the sequence data types like strings, tuples and lists.
- Dictionaries belong to the built-in mapping type.

> NOTE:
>  - Keys must be immutable
>  - Values may be mutable

- Creating an empty dictionary

	```
	In [1]: dict = {}
	
	In [2]: dict
	Out[2]: {}
	```

- Declaring dictionary

	```
	In [4]: phonetic = dict(a='alfa',b='bravo',c='charlie',d='delta',e='echo',f='foxtrot',g='golf',h='hotel',i='india',j='juliet',k='kilo',l='lima',m='mike',n='november',o='oscar',p='papa',q='qubec',r='romeo',s='sierra',t='tango',u='uniform',v='victor',w='whiskey',x='x-ray',y='yankee',z='zulu')

	In [5]: phonetic
	Out[5]: 
	{'a': 'alfa',
	'b': 'bravo',
	'c': 'charlie',
	'd': 'delta',
	'e': 'echo',
	'f': 'foxtrot',
	'g': 'golf',
	'h': 'hotel',
	'i': 'india',
	'j': 'juliet',
	'k': 'kilo',
	'l': 'lima',
	'm': 'mike',
	'n': 'november',
	'o': 'oscar',
	'p': 'papa',
	'q': 'qubec',
	'r': 'romeo',
	's': 'sierra',
	't': 'tango',
	'u': 'uniform',
	'v': 'victor',
	'w': 'whiskey',
	'x': 'x-ray',
	'y': 'yankee',
	'z': 'zulu'}
	```
	
- Converting a list of tuples into a Dictionary

	```
	In [1]: name_and_ages = [('Alice',32),('Bob',48),('Charlie',28),('Daniel',33)]

	In [2]: d = dict(name_and_ages)
	
	In [3]: d
	Out[3]: {'Alice': 32, 'Bob': 48, 'Charlie': 28, 'Daniel': 33}
	
	```
	
- Copying one dictionary to another

	```
	In [11]: d = dict(goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
	
	In [12]: d
	Out[12]: {'goldenrod': 14329120, 'indigo': 4915330, 'seashell': 16774638}
	
	In [3]: e = d.copy()
	
	In [4]: e
	Out[4]: {'goldenrod': 14329120, 'indigo': 4915330, 'seashell': 16774638}
	```
	
- Updating dictionary using another dictionary

	```
	In [13]: g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)

	In [14]: g
	Out[14]: {'crimson': 14423100, 'khaki': 15787660, 'wheat': 16113331}
	
	In [16]: d.update(g)

	In [17]: d
	Out[17]: 
	{'crimson': 14423100,
	'goldenrod': 14329120,
	'indigo': 4915330,
	'khaki': 15787660,
	'seashell': 16774638,
	'wheat': 16113331}
	```

- Looping through the keys of a dictionary

	```
	for key in phonetic:
		print(key)
	```

- Looping through the values of a dictionary

	```
	for key in phonetic:
		print(phonetic[key])
		
	for value in phonetic.values():
		print value
	```
	
- Looping through the keys and values of a dictionary

	```
	for key in phonetic:
		print("{key} => {value}".format(key=key, value=phonetic[key]))
	```