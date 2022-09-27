"""
Create a running Python project that can take two dates as input, and then
calculate the amount of time between them.
Examples:
Input : 22/2/1970 , 22/2/1980
Output : 10 Years, 0 Months, 0 Days
"""
import datetime
strdate1 = input('Enter the frist date')
strdate2 = input('Enter the second date')

year1, month1, day1 = map(int, strdate1.split('/'))
date1 = datetime.date(day1,month1,year1)

year2, month2, day2 = map(int, strdate2.split('/'))
date2 = datetime.date(day2,month2,year2)


year =abs( date1.year - date2.year)
month =abs( date1.month - date2.month)
day = abs(date1.day - date2.day)
print('{} Years, {} Months, {} Days'.format(year,month,day)) 