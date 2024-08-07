# Python program to convert
# date to timestamp


import time
import datetime


string = "15/02/2104"
print(time.mktime(datetime.datetime.strptime(string,"%d/%m/%Y").timetuple()))