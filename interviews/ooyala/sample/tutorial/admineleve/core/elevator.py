from collections import namedtuple
from threading import Thread
import collections
class Elevator:
	poolStruct = namedtuple("poolStruct", "up down")
	current_floor=1
	next_floor=1
	destination_floor=1
	is_open_doors=False
	status=2 # 2 idle, 1 up, 0 down
	pool_request=poolStruct(up=collections.OrderedDict(), down=collections.OrderedDict())
	n=0
	# constuctor to instance an elevator with the number n_
	def __init__(self,n_):
		self.n=n_
		#print "Elevator " + str(n_) +" created"
	# method to climb one floor at time
	def go_up(self):
		self.status=1
		self.current_floor+=1
		
	# method to declimb one floor at time
	def go_down(self):
		self.status=0
		self.current_floor-=1

	# method to sent a request to open doors in the floor
	def send_request(self,floor):
		if(floor<self.current_floor):
			if not floor in self.pool_request.down_arr:
				self.pool_request.down[floor]=1
		else:
			if not floor in self.pool_request.up_arr:
				self.pool_request.up[floor]=1
		self.set_destination()

		if self.status==2:
			thread = Thread(target = self.go_destination)
    			thread.start()

	def set_destination(self):
		if self.status==2:# if is idle
			if self.current_floor!=1 and len(self.pool_request.up)==0 and len(self.pool_request.down)==0:
				self.destination_floor=1
			if self.current_floor==1 and len(self.pool_request.up)!=0:
				self.destination_floor=self.pool_request.up.keys()[0]
		elif self.status==1: #if is up
			if len(self.pool_request.up)!=0:
				self.destination_floor=self.pool_request.up.keys()[0]
			else: # change sense 
				self.destination_floor=self.pool_request.down.keys()[len(self.pool_request.down.keys())-1]
		else:# if is downing 
			if len(self.pool_request.down)!=0:
				self.destination_floor=self.pool_request.down.keys()[len(self.pool_request.down.keys())-1]
			else: # change sense  
				self.destination_floor=self.pool_request.up.keys()[0]
	
	def remove_destination(self, floor):
		if self.status==1: #is up
			if floor!=self.pool_request.up.keys()[0]:
				if not self.pool_request.up.keys()[0] in self.pool_request.down:
					self.pool_request.down[self.pool_request.up.keys()[0]]=1
				self.pool_request.up.remove(self.pool_request.up.keys()[0])
			self.pool_request.up.remove(floor)			
		elif self.status==0: #is down
			if floor!=self.pool_request.down.keys()[len(self.pool_request.down.keys())-1]:
				if not self.pool_request.down.keys()[len(self.pool_request.down.keys())-1] in self.pool_request.up:
					self.pool_request.up[self.pool_request.down.keys()[len(self.pool_request.down.keys())-1]]=1
				self.pool_request.down.remove(self.pool_request.down.keys()[len(self.pool_request.down.keys())-1])
			self.pool_request.down.remove(floor)
								
	def go_destination(self):
		while self.current_floor!=self.destination_floor:
			if self.current_floor<self.destination_floor:
				self.go_up()
			else:
				self.go_down()
			time.sleep(3)	
		self.is_open_doors=True
		self.remove_destination(self.current_floor)
		if len(self.pool_request.up)==0 or len(self.pool_request.down)==0:		
			self.status=2
		time.sleep(10)
		self.set_destination()
		self.is_open_doors=False
		if self.destination_floor==1 or len(self.pool_request.up)!=0 or len(self.pool_request.down)!=0:
			self.go_destination()
			
	def get_currentFloor(self):
		return self.current_floor

	def get_status(self):
		return self.status

	def get_doorStatus(self):
		return self.is_open_doors
	
	
