# Meta Characters for Regular Expressions

- Basic RegExs:
	1. Alphanumeric / literal characters - (a-zA-Z,0-9,_)

***Important Metacharacters:***
- Features: Metacharacters that helps us to search for strings in text
	1. `*` - matches 0 or more times the preceeding token
	
	> Ex: To search Linux119 - [lL]inux[0-9]*
	>> This will match linux, Linux, linux1, Linux1, linux11, Linux11, linux119, Linux119
