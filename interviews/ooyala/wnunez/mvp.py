#!/usr/bin/python

import sys, getopt
from admin import Admin
from floor import Floor

def printWarning(text):
	print "WARNING: "+text
	
def printInfo(text):
	print "INFO: "+text
	
def print_menu():       ## Your menu design here
	print ""
	print 30 * "-" , "MENU" , 30 * "-"
	print "1. Ask Elevator 1"
	print "2. print Elevators"
	print "3. Exit"
	print 67 * "-"



def main(argv):
	loop=True
	floors=[]
	if len(sys.argv)<3:
		printWarning("usage:\nMVP\t -n = Number of floors\n\t -m= Number of Elevators")
		return 0
	m,n=int(sys.argv[1]), int(sys.argv[2])
	printInfo("received values:"+str(n)+" "+str(m));
	admin=Admin(n,m)
	for i in range(m):
		floors.append(Floor(i,admin))
		
	while loop:          ## While loop which will keep going until loop = False
		admin.printStatusElevators()
		print_menu()    ## Displays menu
		choice = input("Enter your choice [1-3]: ")	
		if choice==1:
			floor, destination = map(int,raw_input(" <floor> <destination floor>\n").split(" "))
			if floor <= m and destination<=m and destination!=floor:
				up_down=1 if destination>floor else 2
				closer_elevator=floors[floor].askResources(up_down)
				print "The elevator " + str(closer_elevator)+ " will attend this request"
				threading.Timer(1, set_floor,[admin.elevators[closer_elevator],floor,destination]).start()
			#routine to ask elevator
		elif choice==2:
			admin.printStatusElevators()
		elif choice==3:
			loop=False

def set_floor(elevator,floor,destination_floor):
	while true:
		if elevator.get_currentFloor()==floor:
			elevator.sentRequest(destination_floor)
			break
		time.sleep(5)
	    	
if __name__ == "__main__":
   main(sys.argv[1:])
   