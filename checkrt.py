#!/usr/bin/env python
"""
# File Name: checkrt.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Tue 28 Apr 2015 05:28:45 PM HKT
# Usage: checkrt.py ip|host
"""

from subprocess import Popen,PIPE
import sys
import logging

#LOGGING CONFIG
logfile = "/var/log/checkrt.log"
logging.basicConfig(filename = logfile, level = logging.INFO, format = '%(asctime)s - %(levelname)s: %(message)s')

#START CHECKING	
ip = sys.argv[1]
logging.info('START checking route to %s' %ip)
p = Popen('mtr -c 100 -r -n %s' %ip, shell = True, stdout = PIPE, stderr = PIPE)
p.wait()
stdoutdata, stderrdata = p.communicate()
if(p.returncode == 0):
	lastline = stdoutdata.splitlines().pop().split()
	loss = float(lastline[2].replace('%',''))
	avg = float(lastline[5])
	if(loss > 10.0 or avg > 50.0):
		logging.warn('the route to %s is not good' %ip)
		logging.warn("here is result of the command mtr with 100 packets\n%s" %stdoutdata)
	else:
		logging.info('checking route to %s DONE' %ip)
elif(stderrdata):
	logging.error(stderrdata)
