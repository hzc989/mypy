#!/usr/bin/env python
#########################################################################
# File Name: checkrt.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Tue 28 Apr 2015 05:28:45 PM HKT
#########################################################################

from subprocess import Popen,PIPE
import sys
import logging

#LOGGING CONFIG
logfile = "/var/log/checkrt.log"
logging.basicConfig(filename = logfile, level = logging.INFO, format = '%(asctime)s - %(levelname)s: %(message)s')
#IP TEST
ip = sys.argv[1]
test = Popen('ping -c 5 %s' %ip,shell = True, stdout = PIPE, stderr = PIPE)
if(test.returncode != 0):
	logging.error('target host unreachable or does not exist!')
	exit(1)
#START CHECKING	
logging.info('START checking route to %s' %ip)
p = Popen('mtr -c 100 -r -n %s' %ip, shell = True, stdout = PIPE, stderr = PIPE)
p.wait()
stdoutdata, stderrdata = p.communicate()
if(stderrdata):
	logging.error(stderrdata)
if(p.returncode == 0):
	lastline = stdoutdata.splitlines().pop().split()
	loss = float(lastline[2].replace('%',''))
	avg = float(lastline[5])
	print loss,avg
	if(loss > 10.0 or avg > 50.0):
		logging.warn('the route to %s is not good' %ip)
		logging.warn("here is result of the command mtr with 100 packets\n%s" %stdoutdata)
	else:
		logging.info('checking route to %s DONE' %ip)
