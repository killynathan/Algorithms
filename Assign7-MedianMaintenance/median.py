# given a stream of numbers in the form of a list, compute the median of the collected 
# numbers every time you receive a new number
# done using a max heap that stores the smaller half of the values
# and a min heap that stores the bigger half of the values
import heapq

# just a normal heap that multiplies values by -1 before pushing and same when popping
# only works for numbers
# doesnt check boundries
class MaxHeap(object):
	def __init__(self):
		self.heap = []

	def push(self, element):
		element = element * -1
		heapq.heappush(self.heap, element)

	def pop(self):
		return (-1 * heapq.heappop(self.heap))

	def peekMax(self):
		return (-1 * self.heap[0])

	def isEmpty(self):
		return len(self.heap) == 0

def findMediansAtEachInsert(list):
	# init counter low heap and max heap and median tracker at each step
	lowH = MaxHeap()
	highH = []
	counter = 0 # keeps track of the difference in size of two heaps
	medians = []

	# loop through all elements
	for elem in list:
		
		# insert next element
		if lowH.isEmpty() or elem > lowH.peekMax():
			heapq.heappush(highH, elem)
			counter -= 1
		else:
			lowH.push(elem)
			counter += 1

		# balance if necessary
		if counter >= 2:
			heapq.heappush(highH, lowH.pop())
			counter -= 2

		if counter <= -2:
			lowH.push(heapq.heappop(highH))
			counter += 2

		# get median
		if counter is 1:
			medians.append(lowH.peekMax())
		else:
			medians.append(highH[0])

	return medians

test = [1,9,2,8,3,7,4,6,5]
print(findMediansAtEachInsert(test))
