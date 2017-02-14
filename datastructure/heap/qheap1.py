# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/qheap1

class heap:
    aHeap=[]
    min_=1000000000
    
    def __init__(self,arrayInit):
        self.aHeap=arrayInit
        
    def _add(self, value):
        self.aHeap.append(value)
        self.min_=value if value < self.min_ else self.min_
            
            
    def _delete(self, value):        
        self.aHeap.remove(value)
        if self.min_==value:
            self.min_=self._get_min()
    
    def _print(self):
        for item in self.aHeap:
            print item,
        print ""
        
    def _print_min(self):        
        print self.min_
        
    def _get_min(self):
        minValue=1000000000
        if len(self.aHeap)>0:
            minValue=self.aHeap[0]
            for item in self.aHeap:
                if minValue>item:
                    minValue=item
            return minValue
        return minValue
            
        
n=int(raw_input())
querys=[]
for i in range(0,n):
    querys.append(map(int,raw_input().split(" ")))

heap_= heap([])

for query in querys:
    if query[0]==1:
        heap_._add(query[1])
    elif query[0]==2:
        heap_._delete(query[1])
    else:
        heap_._print_min()
        
