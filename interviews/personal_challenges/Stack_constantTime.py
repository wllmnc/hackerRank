 class Stack_:
     arr_=[]
     ordered_arr=[]
     max_val=0
     
     def push(self,item):
         self.arr_.appened(item)  
         if item>=self.ordered_arr[len(self.ordered_arr)-1]:
             self.ordered_arr.appened(item)
         if self.max_val< item:
            self.max_val=item          
     
     def pop(self):
         item=self.arr_[len(arr_)-1]
         if self.max_val==item:
             self.ordered_arr.pop()
             self.max_val=self.ordered_arr[self.len(ordered_arr)-1]
         self.arr_.pop()
         return item
         
     def getMaxItem(self):
         return -1 if len(self.ordered_arr)==0 else self.max_val
         
