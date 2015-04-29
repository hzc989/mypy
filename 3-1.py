#########################################################################
# File Name: 3-1.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Wed 31 Dec 2014 02:28:40 PM HKT
#########################################################################
#!/usr/bin/env python
num=int(raw_input('please input an integer \n'))
sum=0
if num !=0:
	for num in range(0,num):
		if num % 3 == 0 :
			sum += num
		if num % 5 == 0 :
			sum += num
	print sum
