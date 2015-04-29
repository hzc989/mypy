#########################################################################
# File Name: 3-4.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Wed 31 Dec 2014 05:16:34 PM HKT
#########################################################################
#!/usr/bin/env python
n = int(raw_input("please input an integer: "))
n_new=0
n_tmp=0
i=0
while n / 10 !=0:
	n_tmp=n%10
	n_new=n_new*10+n_tmp*10
	n=n/10
	i+=1
n_new+=n
print n_new
print i
#实现倒序数字输出的功能 例21345-54312
