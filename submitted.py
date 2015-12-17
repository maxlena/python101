

# ASSIGNMENT:  Finding Numbers in a Haystack
# ----------------------------------------------------------
# Extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# * A sample file where we give you the sum for your testing 
# * The actual data you need to process for the assignment.
#     Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 116 values with a sum=597873)
#     Actual data: http://python-data.dr-chuck.net/regex_sum_190215.txt (There are 61 values and the sum ends with 126)
# 
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program.
#  
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. 
# Here is a sample of the output you might see:
# 
#             Why should you learn to write programs? 7746
#             12 1929 8827
#             Writing programs (or programming) is a very creative 
#             7 and rewarding activity.  You can write programs for 
#             many reasons, ranging from making your living to solving
#             8837 a difficult data analysis problem to having fun to helping 128
#             someone else solve a problem.  This book assumes that 
#             everyone needs to know how to program ...
#              
# The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be 
# any number of numbers in each line (including none).
# 
# The basic outline of this problem is to read the file, 
# look for integers using the re.findall(), 
#     looking for a regular expression of '[0-9]+' 
#         and then converting the extracted strings to integers 
#             and summing up the integers. 
#  ANSWER <- 298126

import os

print os.getcwd()
os.chdir("")
os.getcwd()
os.listdir(os.curdir)

import re
 
fname = 'regex_sum_190215.txt'

fh = open(fname)
total_sum = 0
for line in fh:
    numbers_in = re.findall('([0-9]+)', line)
    for i in numbers_in: 
        total_sum += int(i)  
 
print str(total_sum) 

#------------------------------------
# Quiz: Regular Expressions (wk2)
#         
#         import re
#         
#         x = 'From: Using the : character'
#         x1 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#         
#         y = re.findall('^F.+:', x)
#         y1 = re.findall('\S+?@\S+', x1)
#         print y, y1

