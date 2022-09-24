"""
Create a running Python project that can take two dates as input, and then
calculate the amount of time between them.
Examples:
Input : 22/2/1970 , 22/2/1980
Output : 10 Years, 0 Months, 0 Days
"""
# imports
import datetime

# input dates
print ('This program will calculate the amount of time between two dates of your choice !!!')
strdate1 = input('Enter a date in DD/MM/YYYY format ')
strdate2 = input('Enter another date in DD/MM/YYYY format ')

# split the string and change the type to int
year, month, day = map(int, strdate1.split('/'))
date1 = datetime.date(day,month,year)
year, month, day = map(int, strdate2.split('/'))
date2 = datetime.date(day,month,year)

# find the diffrence 
year = date1.year - date2.year
month = date1.month - date2.month
day = date1.day - date2.day

# print the result
print('{} Years, {} Months, {} Days'.format(year,month,day))
