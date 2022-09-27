"""
Create a running Python project to check if all digits of a number divide it; given a
number n, find whether all digits of n divide it or not.
Input : 128
Output : Yes
128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Input : 130
Output : No 
"""
number = input()
intnum = int(number)

flag = True
counter = 0

strprint = ''

for i in number:
    digit = int(i)
    if digit == 0 or intnum % digit != 0:
        flag = False
        break
    else:
        if counter + 1 == len(number):
            strprint += 'and {} % {} == 0'.format(intnum,digit)
        else:
            strprint += '{} % {} == 0, '.format(intnum,digit)
            counter += 1
            
if flag == False: 
    print('No')
else:
    print('Yes')
    print(strprint)
