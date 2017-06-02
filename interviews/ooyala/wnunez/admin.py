from elevator import Elevator

class Admin:
	n,m=0,0
	elevators=[]
	#to create this admin elevator we must specify the number of floors and elevators
	def __init__(self,  elevators, floors):
		self.n=elevators
		self.m=floors
		for i in range(self.n):
			self.elevators.append(Elevator(i,self.m))
		
	def get_closerElevator(self,floor, up_down):
		close_elevator=0
		min_distance=abs(1-floor)
		for elevator in self.elevators:
			if min_distance < abs(floor-elevator.get_currentFloor()) and (elevator.get_status==up_down or elevator.get_status==0):
				close_elevator=elevator.get_numElevator()
		self.elevators[close_elevator].sentRequest(floor)
		return close_elevator
		
	def printStatusElevators(self):
		for elevator in self.elevators:
			print "- E"+str(elevator.get_numElevator())+" CF:"+str(elevator.get_currentFloor()),
		print ""
		
    