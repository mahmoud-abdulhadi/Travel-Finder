import heapq 

class Heap(object):
	#Min heap 

	def __init__(self):
		self._values = [] 


	def push(self,value):
		#Push the value item onto the heap , which will sort it in O(logn)
		heapq.heappush(self._values,value)



	def pop(self):
		#Pop and return the smallest item from the heap 
		return heapq.heappop(self._values)

	def __len__(self):
		return len(self._values)