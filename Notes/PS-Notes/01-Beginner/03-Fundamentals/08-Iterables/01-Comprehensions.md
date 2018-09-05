# Comprehensions

- Comprehensions are constructs that allow sequences to be built from other sequences.
- Python 2.0 introduced list comprehensions and Python 3.0 comes with dictionary and set comprehensions.

# List Comprehensions

- A list comprehension consists of the following parts:
- An Input Sequence.
- A Variable representing members of the input sequence.
- An Optional Predicate expression.
- An Output Expression producing elements of the output list from members of the Input Sequence that satisfy the predicate.

	```
	In [1]: words = "We are trying to learn Python list comprehensioning".split()
	
	In [2]: words
	Out[2]: ['We', 'are', 'trying', 'to', 'learn', 'Python', 'list', 'comprehensioning']
	
	In [3]: [len(word) for word in words]
	Out[3]: [2, 3, 6, 2, 5, 6, 4, 16]
	In [4]: lengths = [len(word) for word in words]                                                                                                        
	
	In [5]: wordLengths = []
	
	In [6]: for word in words:
	...:     wordLengths.append(len(word))
	...:     
	
	In [7]: lengths
	Out[7]: [2, 3, 6, 2, 5, 6, 4, 16]
	
	In [8]: wordLengths
	Out[8]: [2, 3, 6, 2, 5, 6, 4, 16]
	```
	
# Set Comprehensions

- Set comprehensions allow sets to be constructed using the same principles as list comprehensions
- The only difference is that resulting sequence is a set.
- Say we have a list of names.
- The list can contain names which only differ in the case used to represent them, duplicates and names consisting of only one character.
- We are only interested in names longer then one character and wish to represent all names in the same format:
- The first letter should be capitalised, all other characters should be lower case.
	
	```
	In [1]: from math import factorial
	
	In [2]: f = [len(str(factorial(x))) for x in range(20)]
	
	In [3]: f
	Out[3]: [1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]
	
	In [4]: fs = {len(str(factorial(x))) for x in range(20)}
	
	In [5]: fs
	Out[5]: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}
	```
	
# Dictionary Comprehensions

- Say we have a dictionary the keys of which are characters and the values of which map to the number of times that character appears in some text.
- The dictionary currently distinguishes between upper and lower case characters.
- Here we have a dictionary which contains Country to Capital mapping.
- Let us try to reverse that to Capital to Country
	
	```
	In [1]: from pprint import pprint as pp
	
	In [2]: country_to_capital = {'United Kingdon': 'London',
	...:                       'Brazil': 'Brazillia',
	...:                       'Morocco': 'Rabbat',
	...:                       'Sweden': 'Stockholm'}
	
	In [3]: capital_to_country = {capital: country for country, capital in country_to_capital.items()}
	
	In [4]: capital_to_country
	Out[4]: 
	{'Brazillia': 'Brazil',
	'London': 'United Kingdon',
	'Rabbat': 'Morocco',
	'Stockholm': 'Sweden'}
	```
	
- The below example will demonstrate how can we get the first word based on alphabetical order
	
	```
	In [5]: words = ["hi", "hello", "foxtrot", "hotel"]
	
	In [6]: {x[0]: x for x in words}
	Out[6]: {'f': 'foxtrot', 'h': 'hotel'}
	```
	
- `zip()`

	```
	>>> sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
	>>> monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
	>>> for item in zip(sunday, monday):
	...     print(item)
	... 
	(12, 13)
	(14, 14)
	(15, 14)
	(15, 14)
	(17, 16)
	(21, 20)
	(22, 21)
	(22, 22)
	(23, 22)
	(22, 21)
	(20, 19)
	(18, 17)
	>>> for sun, mon in zip(sunday, monday):
	...     print("Average =", (sun + mon) / 2)
	... 
	Average = 12.5
	Average = 14.0
	Average = 14.5
	Average = 14.5
	Average = 16.5
	Average = 20.5
	Average = 21.5
	Average = 22.0
	Average = 22.5
	Average = 21.5
	Average = 19.5
	Average = 17.5
	>>> tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]
	>>> for temps in zip(sunday, monday, tuesday):
	...     print("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(min(temps), max(temps), sum(temps) / len(temps)))
	... 
	min= 2.0, max=13.0, average= 9.0
	min= 2.0, max=14.0, average=10.0
	min= 3.0, max=15.0, average=10.7
	min= 7.0, max=15.0, average=12.0
	min= 9.0, max=17.0, average=14.0
	min=10.0, max=21.0, average=17.0
	min=11.0, max=22.0, average=18.0
	min=12.0, max=22.0, average=18.7
	min=10.0, max=23.0, average=18.3
	min= 9.0, max=22.0, average=17.3
	min= 8.0, max=20.0, average=15.7
	min= 8.0, max=18.0, average=14.3
	```
	
	