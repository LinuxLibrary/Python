# Dictionaries

- Converting a list of tuples into a Dictionary

	```
	In [1]: name_and_ages = [('Alice',32),('Bob',48),('Charlie',28),('Daniel',33)]

	In [2]: d = dict(name_and_ages)
	
	In [3]: d
	Out[3]: {'Alice': 32, 'Bob': 48, 'Charlie': 28, 'Daniel': 33}
	
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
	
- Copying one dictionary to another

	```
	In [11]: d = dict(goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
	
	In [12]: d
	Out[12]: {'goldenrod': 14329120, 'indigo': 4915330, 'seashell': 16774638}
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
	In [20]: for key in phonetic:
	   ....:	 print("{key} => {value}".format(key=key, value=phonetic[key]))
	   ....:
	a => alfa
	c => charlie
	b => bravo
	e => echo
	d => delta
	g => golf
	f => foxtrot
	i => india
	h => hotel
	k => kilo
	j => juliet
	m => mike
	l => lima
	o => oscar
	n => november
	q => qubec
	p => papa
	s => sierra
	r => romeo
	u => uniform
	t => tango
	w => whiskey
	v => victor
	y => yankee
	x => x-ray
	z => zulu
	```