from .elevator import Elevator

class Admin:
	#globalVariables
	#n-> elevators, m-> floors
	n,m=1,1
	#arrays of elevators
  	elevators=[]

	# constructor of this object, set the GV n,m and fill the elevators array
	def __init__(self,n_,m_):
		self.n=n_
		self.m=m_
		print "Admin will handle " + str(self.n) + " elevators for "+ str(self.m)+ " Floors"
		for i in range(1,self.n+1):
			self.elevators.append(Elevator(i))
			print self.get_information_elevator(i)

	# ask to fixed elevator the request for a floor
	def set_destination_elevator(self,elevator_num,floor):
		if floor<=self.m:
			elevator_status=self.validate_elevator(elevator_num)
			if elevator_status=="":
				self.elevators[elevator_num-1].send_request(floor,2)
			else:
				print elevator_status
		else:
			print "floor " + str(floor)+ " is out of range max "+ str(self.m)

	
	# return the information used by the view about that specific elevator 
	def get_information_elevator(self, elevator_num):
		elevator_status=self.validate_elevator(elevator_num)
		ans=[]
		if elevator_status=="":
			elevator=self.elevators[elevator_num-1]
			ans.append(elevator_num)
			ans.append(elevator.get_currentFloor())
			ans.append(1 if elevator.is_doorOpen() else 0)
			ans.append(elevator.get_currentSense())
		return ans

	# validate if is a valid elevator
	def validate_elevator(self, elevator_num):
		ans=""
		if elevator_num>self.n:
			ans=" Elevator " + str(elevator_num)+ " is out of range "
		return ans
	# determine which could be the better elevator to attend a request, taking in mind the following cases:
	#     only can respond elevator with the same sense at time to ask or iddle elevators
	#     we have to consider:
	#	*		the spended time between each floor
	#	*		spended time when a elevator opend doors
	#	*		if a elevator has destination on queue, we have to consider the worst case escenario, is when it open doors in each floor before to reach the new destinarion:
	# 	*		the iddle elevator can up and down only spending the time between floors
	#     taking in count the previous information, we will be able to decide who will spend less time to reach to this destination
	
	def ask_resources(self,floor,up_down):
		best_elevator=0
		time_between_floors=3
		time_openDoors=10
		min_distance=abs(0-floor)
		min_cost=min_distance*time_between_floors
                print floor,up_down,
		for elevator in self.elevators:
			print elevator.get_status(),elevator.get_status()==up_down
			if (elevator.get_status()==up_down or elevator.get_status()==2): # if the elevator has the same sense
				min_cost_candidate=abs(floor-elevator.get_currentFloor())*time_between_floors
				if elevator.get_status()!=2:
					min_cost_candidate+=abs(floor-elevator.get_currentFloor())*time_openDoors
				if min_cost_candidate<min_cost:
					print "best candidate replaced " + str(elevator.get_numElevator()-1)
					min_cost=min_cost_candidate
					best_elevator=elevator.get_numElevator()-1
		self.elevators[best_elevator].send_request(floor,up_down)
		print "elevator selected to dispatch floor:" + str(floor) + " is "+ str(best_elevator)
		return best_elevator
		
