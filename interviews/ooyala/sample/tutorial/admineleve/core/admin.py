from elevator import Elevator

class Admin:
	n,m=1,1
  	elevators=[]

	def __init__(self,n_,m_):
		self.n=n_
		self.m=m_
		print "Admin will handle " + str(self.n) + " elevators for "+ str(self.m)+ " Floors"
		for i in range(1,self.n+1):
			self.elevators.append(Elevator(i))
			print self.get_information_elevator(i)

	def set_destination_elevator(self,elevator_num,floor):
		if floor<=self.m:
			elevator_status=self.validate_elevator(elevator_num)
			if elevator_status=="":
				self.elevators[elevator_num-1].send_request(floor)
			else:
				print elevator_status
		else:
			print "floor " + str(floor)+ " is out of range"
	
	def get_information_elevator(self, elevator_num):
		elevator_status=self.validate_elevator(elevator_num)
		if elevator_status=="":
			elevator=self.elevators[elevator_num-1]
			elevator_status+=" Elevator - "+ str(elevator_num)
			elevator_status+=" Current floor - " + str(elevator.get_currentFloor())
			elevator_status+=" Status - " + ("UP" if elevator.get_status()==1 else "Down" if elevator.get_status()==0 else "IDLE")		
			elevator_status+=" Door is - " +  ("Open" if elevator.get_doorStatus() else "Close")
		return elevator_status

	def validate_elevator(self, elevator_num):
		ans=""
		if elevator_num>self.n:
			ans=" Elevator " + str(elevator_num)+ " is out of range "
		return ans
	
	def ask_resources(self,floor,up_down):
		closer_elevator=0
		min_distance=abs(1-floor)
		for elevator in self.elevators:
			if min_distance < abs(floor-elevator.get_currentFloor()) and (elevator.get_status==up_down or elevator.get_status==0):
				closer_elevator=elevator.get_numElevator()
		self.elevators[closer_elevator].send_request(floor)
		return closer_elevator
		
