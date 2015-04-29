#########################################################################
# File Name: bmi.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Sun 14 Dec 2014 10:59:57 AM HKT
#########################################################################
#!/usr/bin/env python
weight=float(input("please input your weight:"))
height=float(input("please input your height:"))
BMI=weight/(height**2)
print format(BMI,".2f")
