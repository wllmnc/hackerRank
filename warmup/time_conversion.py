#https://www.hackerrank.com/challenges/time-conversion
#!/bin/python

import sys

time = raw_input().strip()
plus=0
if "PM" in time:
    plus=12
time=time.replace("PM","").replace("AM","")
aTime=time.split(":")

if aTime[0]== "12":
    if plus==0:
        aTime[0]="0"
    else:
        plus=0
newHour=int(aTime[0])+plus
print str(("0"+str(newHour)) if newHour<10 else str(newHour))+":"+aTime[1]+":"+aTime[2]
          
