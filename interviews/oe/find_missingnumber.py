5,3,6,7,1,2,4,9
#develop in less than 10 minutes a solution to find which is the missing number from a list of elements on the list
def whichnumberismissing(arr_):
	arr_.sort() //nlgn
	#Arr_b[len+1];
	#for i in range(1,len(len_)+1):
	#	  Arr_b[arr_i] = arr_[i];

	for i in range(1,len(len_)+1):
		if i!=arr_[i]:
			Return i
	Return 0
#I aslo designed another version which use hashmaps to store the data
#the complexity will be linear in that case
# for each element on the array, add it to the hashmap as the follow couple (value, 1) we dont care the stored value at the hashmap
# then make a loop from 1 to len(array)
#   if the value isnt on the HM
#        return iterator
#the cost to use a HP will be constant and we depend of the size of array then O(n) wrost case escenario
