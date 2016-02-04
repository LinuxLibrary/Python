#!/usr/bin/python

def digit_sum(n): #define our funtion
    digit_list = [] #create a new empty list
    digit_string = str(n) #convert digits to strings
    for i in digit_string: #runs through the numbers in list of strings
        digit_list.append(i) #adds the numbers(strings) to the new list 
        int_list = map(int, digit_list) #converts every string to an integer from the digit_list
        sum_list = sum(int_list) #adds all of the values from the list
    return sum_list    #returns the final list with our answer
print digit_sum(1500)
