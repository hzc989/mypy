#########################################################################
# File Name: 3-2.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Wed 31 Dec 2014 02:46:22 PM HKT
#########################################################################
#!/usr/bin/env python

#1901.01.01 is Tuesday
#totally n Sundays on the first day of every month.
n=0
#judge the Leap Year
for year in range(1901,2001):
	#is a Leap Year
	if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0 :
		#the day after 1901.01.01
		day=0
		#for Feb
		day+=31
		#5 day after Tuesday is Sunday
		if day % 7 == 5 :
			n+=1
		#for Mar
		day+=29
		if day % 7 == 5:
			n+=1
		#for Apri
		day+=31
		if day % 7 == 5:
			n+=1
		#for May
		day +=30
		if day % 7 == 5:
			n+=1
		#for Jun
		day +=31
		if day % 7 == 5:
			n+=1
		#for July
		day +=30
		if day % 7 == 5:
			n+=1
		#for August
		day +=31
		if day % 7 == 5:
			n+=1
		#for Sept.
		day +=31
		if day % 7 == 5:
			n+=1
		#for Oct.
		day +=30
		if day % 7 == 5:
			n+=1
		#for Nov.
		day +=31 
		if day % 7 == 5:
			n+=1
		#for Dec.
		day +=30
		if day % 7 == 5:
			n+=1
		#for Jan.
		day +=30
		if day % 7 ==5:
			n+=1		
	#NOT leap year
	else:
		#the day after 1901.01.01
		day=0
		#for Feb
		day+=31
		#5 day after Tuesday is Sunday
		if day % 7 == 5 :
			n+=1
		#for Mar
		day+=28
		if day % 7 == 5:
			n+=1
		#for Apri
		day+=31
		if day % 7 == 5:
			n+=1
		#for May
		day +=30
		if day % 7 == 5:
			n+=1
		#for Jun
		day +=31
		if day % 7 == 5:
			n+=1
		#for July
		day +=30
		if day % 7 == 5:
			n+=1
		#for August
		day +=31
		if day % 7 == 5:
			n+=1
		#for Sept.
		day +=31
		if day % 7 == 5:
			n+=1
		#for Oct.
		day +=30
		if day % 7 == 5:
			n+=1
		#for Nov.
		day +=31 
		if day % 7 == 5:
			n+=1
		#for Dec.
		day +=30
		if day % 7 == 5:
			n+=1
		#for Jan.
		day +=30
		if day % 7 ==5:
			n+=1
print n
