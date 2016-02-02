#!/usr/bin/python

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Chicken Grilled'] = 240.00
menu['Methi Paneer'] = 60.00
menu['Paneer Masala'] = 90.00

print "There are " + str(len(menu)) + " items on the menu."
print menu
