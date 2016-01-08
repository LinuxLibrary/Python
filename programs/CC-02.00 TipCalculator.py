#!/usr/bin/python

meal = 44.50
tax = 6.75 / 100
tip = 0.15

#meal_tax = meal + meal * tax
#total = meal_tax + meal * tip
meal = meal + meal * tax
total = meal + meal * tip

print ("%.2f" %total)
