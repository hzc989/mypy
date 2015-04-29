#########################################################################
# File Name: 3-2.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Wed 31 Dec 2014 04:20:26 PM HKT
#########################################################################
#!/usr/bin/env python
import math
n=int(raw_input("please input an integer: "))
sum=0
for i in range(2,n+1):
	for j in range(2,i):
		if i % j == 0:
			break # this i is NOT a prime
	else:
		sum+= i
print sum
