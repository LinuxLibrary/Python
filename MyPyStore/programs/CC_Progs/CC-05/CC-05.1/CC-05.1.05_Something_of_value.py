#!/usr/bin/python

prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}

stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

total = 0

for fruit in prices:
    print fruit
    print "price: %s" % prices[fruit]
    print "stock: %s" % stock[fruit]
    fruits_price = prices[fruit] * stock[fruit]
    total = total + fruits_price
print total
