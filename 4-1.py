#########################################################################
# File Name: 4-1.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Mon 05 Jan 2015 09:23:07 AM HKT
#########################################################################
#!/usr/bin/env python
def f(n):
	re=0
	a=0
	b=1
	i=0
	sum=0
	while re < n :
		if i==0 :
			re=0
		elif i==1 :
			re=1
		elif i > 1 :
			if re % 2== 0:
				sum+=re
			re=a+b
			b=a
			a=re
		i+=1
	print sum


	
	
	
	
input=int(raw_input('please input an integer: '))
f(input)

