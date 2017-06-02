class Floor:
	requests=[]
	m=0
	admin=0
	#to create this elevator we must specify the number of floors
	def __init__(self,floor,admin):
		self.m=floor
		self.admin=admin
		print "Created Floor "+str(self.m),
	
	def askResources(self,up_down):
		self.requests.append(up_down)
		elevator=self.admin.get_closerElevator(self.m,up_down)
		" The request will attent by elevator "+ str(elevator)
		self.requests.remove(up_down) # Deleted the code to 
		return elevator