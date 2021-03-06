# -Problem 1_4.py *- coding: utf-8 -*-

"""
Problem 1_4:
Write a function 'problem1_4(miles)' to convert miles to feet. There are
5280 feet in each mile. Make the print out a statement as follows:
"There are 10560 feet in 2 miles."  Except for the numbers this statement 
should be exactly as written.

Tip: Watch the spacing before and after your numbers.  Make sure that it is 
just one space or the auto-grader may not give you credit.
"""
#%%
def problem1_4(miles):
    feet = 5280 * miles
    print("There are",feet,"feet in",miles,"miles.")
    
#%%
"""
Test run. Note that the grader program will use different numbers:

problem1_4(5)
There are 26400 feet in 5 miles.
"""