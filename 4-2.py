#########################################################################
# File Name: 4-2.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Mon 05 Jan 2015 10:52:48 AM HKT
#########################################################################
#!/usr/bin/env python

#1800.01.01 Wednesday

year = int(raw_input('plz input the year: '))
month= int(raw_input('plz input the month: '))

#IS_LEAP_YEAR?

def is_leap(y):
	if y % 4 == 0 and y % 100 !=0:
		return True
	elif y%400 ==0:
		return True
	else:
		return False
leap=0
noleap=0
for i in range(1800,year):
	if (is_leap(i)):
		leap+=1
	i+=1
noleap=year-1800-leap

#the summary days after 1800.01.01  
day = 365*noleap + 366*leap

#Cal the last year 
for m in range(1,month+1):
	if m in (1,3,5,7,8,10,12):
		day +=31
	if m in (4,6,9,11):
		day +=30
	else :
		if(is_leap(year)):
			day+=29
		else:
			day+=28
	m+=1
weekday=day % 7

print weekday

