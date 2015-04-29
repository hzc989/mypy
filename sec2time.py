#########################################################################
# File Name: sec2time.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Sun 14 Dec 2014 03:26:20 PM HKT
#########################################################################
#!/usr/bin/env python
sec=int(input("please input second:"))
if sec>0:
	hr=sec/3600
	min=(sec%3600)/60
	s=sec%3600%60
	print("%d %d %d" %(hr,min,s))
else:
	print 'you should input a positive num!'
