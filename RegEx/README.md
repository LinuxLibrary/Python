# Regular Expressions

***Features***

- Regular Expressions are supported by many applications
	- GREP - Line parsing tool which parses mathced test and/or RegEx
	- AWK - Field parsing tool which parses mathced test and/or RegEx
	- SED - Stream Editor - Permits modifications of the text streams
	- PERL - Supports normal text and/or RegEx matches
	- PYTHON - Supports normal text and/or RegEx matches
	- PHP - Supports normal text and/or RegEx matches
	
		> NOTE: Supports Perl compatible RegEx

	- .Net - Supports normal text and/or RegEx matches
	- Java - Supports normal text and/or RegEx matches
	- JavaScript -  Supports normal text and/or RegEx matches
- Ability to describe search patterns concisely
	- Search for `linux (or) Linux`: `[lL]inux`
- Reduces passes over text files - in particular large files
- Uses meta-characters and regular (literal[A-Za-z,0-9,_]) characters to describe search patterns
- First match wins unless quantifiers are used (typical RegEx algorithms)
- Searches for characters at beginning and end of the string using:
	- `^` - Caret - Anchor for the beginning of a string
	- `$` - Dollar - Anchor for the end of a string
	- `^$` - Finds empty lines
- Ability to define character classes and sets - ranges of characters - 0-9, A-Z, a-z
	- Search for `Linux119`: `[lL]inux[0-9][0-9][0-9]`
- Reference predefined (shorthand) character sets - i.e. `\b`: `(word boundary)`
- Negate character classes and sets using - `^`
- Supports alternation of characters - [cat|dog] - | = OR
- Supports alternation of words or RegEx - (cat|dog) - matches whole word
- Supports operational meta characters - ?, *, +, . (Matches any character except new line)
- Supports repetition via 3 quantifiers
	- * - matches 0 or more times
	- + - matches 1 or more times
	- {} 
		- {n} - Matches `n` times
		- {min,max} - Matches at least min times and at most  max times

		```
		Linux119 - [lL]inux[0-9]{1,3}
		```
