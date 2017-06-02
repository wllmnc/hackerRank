from collections import namedtuple
from threading import Thread
import time

import collections
class Elevator:
        poolStruct = namedtuple("poolStruct", "up down")
	current_floor=1
	next_floor=1
	destination_floor=1
	destination_sense=2
	is_open_doors=False
	status=2 # 2 idle, 1 up, 0 down
	pool_request=None
	n=0
	# constuctor to instance an elevator with the number n_
	def __init__(self,n_):
		self.n=n_
		poolStruct = namedtuple("poolStruct", "up down")
		self.pool_request=poolStruct(up=collections.OrderedDict(), down=collections.OrderedDict())
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
	def send_request(self,floor,sense):
		if(floor<self.current_floor):
			if not floor in self.pool_request.down:
				self.pool_request.down[floor]=sense
		else:
			if not floor in self.pool_request.up:
				self.pool_request.up[floor]=sense
		self.set_destination()
		if self.status==2:
			thread = Thread(target = self.go_destination)
    			thread.start()
	# method to select the next destination if there is
	def set_destination(self):
		if self.status==2:# if is idle
			if self.current_floor!=1 and len(self.pool_request.up)==0 and len(self.pool_request.down)==0:
				self.destination_floor=1
				self.destination_sense=2
			if self.current_floor==1 and len(self.pool_request.up)!=0:
				self.destination_floor=self.pool_request.up.keys()[len(self.pool_request.up.keys())-1]
				self.destination_sense=self.pool_request.up[self.destination_floor]
		elif self.status==1: #if is up
			if len(self.pool_request.up)!=0:
				self.destination_floor=self.pool_request.up.keys()[len(self.pool_request.up.keys())-1]
				self.destination_sense=self.pool_request.up[self.destination_floor]
			else: # change sense
				self.status=0 
				self.destination_floor=self.pool_request.down.keys()[len(self.pool_request.down.keys())-1]
				self.destination_sense=self.pool_request.up[self.destination_floor]
		else:# if is downing 
			if len(self.pool_request.down)!=0:
				self.destination_floor=self.pool_request.down.keys()[len(self.pool_request.down.keys())-1]
				self.destination_sense=self.pool_request.up[self.destination_floor]
			else: # change sense 
				self.status=1 
				self.destination_floor=self.pool_request.up.keys()[len(self.pool_request.up.keys())-1]
				self.destination_sense=self.pool_request.up[self.destination_floor]

	# when we reach a destination, we deleted this target from the arrays
	def remove_destination(self, floor):
		if self.status==1: #is up
			if floor!=self.pool_request.up.keys()[len(self.pool_request.up.keys())-1]:
				del self.pool_request.up.keys()[len(self.pool_request.up.keys())-1]
			del self.pool_request.up[floor]
		elif self.status==0: #is down
			if floor!=self.pool_request.down.keys()[len(self.pool_request.down.keys())-1]:
				del self.pool_request.down.keys()[len(self.pool_request.down.keys())-1]
			del self.pool_request.down[floor]
								
	# recursive method to preform up and down movements to each elevator until reach the current destination
	def go_destination(self):
		while self.current_floor!=self.destination_floor:
			if self.current_floor<self.destination_floor:
				self.go_up()
			else:
				self.go_down()
			time.sleep(3)	
		self.is_open_doors=True
		if len(self.pool_request.up)!=0 or len(self.pool_request.down)!=0:
			self.remove_destination(self.current_floor)
		time.sleep(10)	# sleep time to simulate the time between floors	
		if len(self.pool_request.up)==0 and len(self.pool_request.down)==0:# we get iddle
			self.status=2
			self.is_open_doors=False
		print " destination " + str(self.destination_floor) + " reached "
		self.set_destination()
		print " new  destination " + str(self.destination_floor) + " "
		print "Up  :"+ str(self.pool_request.up)
                print "Down:"+ str(self.pool_request.down)
	
		# control to determine if we have more destinations of we are iddle and return to floor 1 
		self.is_open_doors=False
		if (self.destination_floor==1 and self.destination_floor!=self.current_floor) or (len(self.pool_request.up)!=0 or len(self.pool_request.down)!=0):
			self.go_destination()

	# methods to return the current state of this object			
	def get_currentFloor(self):
		return self.current_floor

	def get_status(self):
		return self.status

	def is_doorOpen(self):
		return True if self.is_open_doors==1 else False
	
	def get_numElevator(self):
		return self.n	

	def get_currentSense(self):
		return self.destination_sense
