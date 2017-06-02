import Queue
import threading
import time

class Elevator:
	q_elevatorPanel = []
	current_Floor=1
	destination_Floor=1
	status=0  # 0 for waiting, 1 for up, 2 for down
	n=0
	
	#to create this elevator we must specify the number of floors
	def __init__(self,n,floors):
		self.m=floors
		self.n=n
		print "Created Elevator "+str(self.n),
		print "Current floor "+ str(self.get_currentFloor())
    	
    # method to send a request for this elevator
	def sentRequest(self, floor):
	    if self.status==0:
	    	self.q_elevatorPanel.append([floor])
	    elif self.status==1:
	    	if self.current_Floor<floor:
	    		if len(self.q_elevatorPanel)>1:
	    			if not floor in self.q_elevatorPanel[1]:
	    				self.q_elevatorPanel[1].append(floor)
	    				self.q_elevatorPanel[1].sort()
	    		else:
	    			self.q_elevatorPanel.append([floor])
	    	else:
				self.q_elevatorPanel[0].append(floor)
				self.q_elevatorPanel[0].sort()
	    else:# is down
	    	if self.current_Floor>floor:
	    		if len(self.q_elevatorPanel)>1:
	    			if not floor in self.q_elevatorPanel[1]:
	    				self.q_elevatorPanel[1].append(floor)
	    				self.q_elevatorPanel[1].sort()
	    		else:
	    			self.q_elevatorPanel.append([floor])
	    	else:
	    		self.q_elevatorPanel[0].append(floor)
	    		self.q_elevatorPanel[0].sort()
		destination_Floor=self.q_elevatorPanel[0][0]
	    if self.status==0:
	    	self.goTo()
    
    # method to go at the elevator
	def goTo(self):
        #if there are floor on the request queue, to the next floor required.
		if len(self.q_elevatorPanel)>0:
			self.status= 1 if self.current_Floor<self.destination_Floor else 2
		else: #if the queue is empty go to floor 
			self.destination_Floor =1
			self.status=2
		threading.Timer(1, self.goToDestinationFloor).start()
    
    # Method which simule the pass throw the floor until reach our destiny
	def goToDestinationFloor(self):
		if self.status==1:
		    i=self.current_Floor
		    while i!=self.destination_Floor:
				time.sleep(30)
				set_current_floor(i)
				i+=1
		else:
		    i=self.current_Floor
		    while i!=self.destination_Floor:
				time.sleep(30)
				set_current_floor(i)
				i-=1
		#self.status=self.q_elevatorPanel[0];

		if len(self.q_elevatorPanel[0])==0:
			self.q_elevatorPanel.remove(0);
			
     	# if still are floors to dispatch start the process again
		if len(self.q_elevatorPanel):
			self.goTo()
     		
    #method to send the currentFloor  		
	def set_currentFloor(self, floor):
		self.current_Floor=floor
   
    # method to get the current floor of this elevator    	
	def get_currentFloor(self):
		return  self.current_Floor
    	   	
	def get_numElevator(self):
		return self.n
	
	def get_status(self):
		return self.status