#########################################################################
# File Name: 4-3.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Mon 05 Jan 2015 03:16:57 PM HKT
#########################################################################
#!/usr/bin/env python
def hanoi(n,From,Tmp,To):
	if n==1:
		print 'move',n,'from',From,'to',To
	else:
		hanoi(n-1,From,To,Tmp)
		print 'move',n,'from',From,'to',To
		hanoi(n-1,Tmp,From,To)

num=int(raw_input())
hanoi(num,'A','B','C')
