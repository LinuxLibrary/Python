# Python Strings

- Anything enclosed in quotes can be treated as string in Python
- For multiline string we need to enclose that in triple quotes either single or double

```
'''
Python multiline
string
'''
```

- String variables can be concatinated

```
server_name = "dev-r73"
server_type = "redhat"
server_desc = "Server " + server_name + "is using " + server_type
print server_desc
Output: Server dev-r73 is using redhat
```

- Strings can be called in print using `%s`

```
print "Server %s is using %s" % (server_name, server_type)
```

- len() function is used to check the length of the string
	- Length of a string can be indexed starting from `0`

- For more [String Extraction](https://github.com/LinuxLibrary/Python/blob/master/py4sa/ORielly-notes/Chapter-3/02.Built-in-methods-for-str-data-extraction.md)
