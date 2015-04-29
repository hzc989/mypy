#########################################################################
# File Name: apache_log_shelve.py
# Author: Houston Wong
# mail: hzc989@163.com
# Created Time: Wed 20 Aug 2014 02:46:59 PM HKT
#########################################################################
#!/usr/bin/env python
import shelve
import apache_log_parser_regex

logfile=open('/etc/httpd/logs/access_log-20140818','r')
shelve_file=shelve.open('./access.s')

for line in logfile:
	d_line=apache_log_parser_regex.dictify_logline(line)
	try:
		shelve_file[d_line['remote_host']]=\
			shelve_file.setdefault(d_line['remote_host'],0)+\
			int(d_line['bytes_sent'])
	except ValueError:
		##disregard the - data
		continue
logfile.close()
shelve_file.close()

