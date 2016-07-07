#!/usr/bin/python

text = "X-DSPAM-Confidence:    0.8475";
sppos = text.find(' ')
op = text[sppos:len(text)]
print float(op.lstrip())
