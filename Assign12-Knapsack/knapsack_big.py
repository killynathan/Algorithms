# efficient way to solve napsack problem with dynamic programming
def getOptimalValueForKnapsack(filename):
	# get capacity & item list
	num_of_items, capacity, items = getCapacityAndItems(filename)

	# get 1D to keep track of the previous optimal values.
	A = [0 for x in range(capacity + 1)]
	
	# loop through items and get optimal value at each weight
	for i in range(1, num_of_items + 1):
		for j in range(capacity, items[i][1] - 1, -1): # dont need to update if weight of item too high
			A[j] = max(A[j], A[j - items[i][1]] + items[i][0])

	return A[capacity]

# get list where each element is [value, weight]. each item is its index. items start with index 1!
def getCapacityAndItems(filename):
	file_by_line = open(filename, 'r').read().split('\n')
	list_by_items = [line.split(' ') for line in file_by_line]
	items = [[int(item[0]), int(item[1])] for item in list_by_items]
	return items[0][1], items[0][0], items

# testing
print(getOptimalValueForKnapsack('items_small.txt'))
