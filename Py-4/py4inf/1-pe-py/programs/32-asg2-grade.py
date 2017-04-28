#!/usr/bin/python

inp = raw_input("Enter Score: ")
score = float(inp)

if score >= 0.9 and score <= 1.0:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
elif score < 0.6 and score > 0.0:
    grade = 'F'
else:
    print "Please input a value between 0.0 and 1.0"
    
print grade
