# the ineficient way to solve the knapsakc problem using Dynammic Programming
def getOptimalValueForKnapsack(filename):
	# get capacity & item list
	num_of_items, capacity, items = getCapacityAndItems(filename)

	# get 2D array to store optimal value at each step
	matrix = [[0 for x in range(capacity + 1)] for y in range(num_of_items + 1)] # plus one because want a 0 column and row
	
	# double loop through all items and weights
	for i in range(1, num_of_items + 1): # for each item
		for j in range(capacity + 1): # for each weight from 0 to capacity
			if j < items[i][1]:
				matrix[i][j] = matrix[i - 1][j]
			else:
				matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - items[i][1]] + items[i][0])

	# return optimal value
	return matrix[num_of_items][capacity]

# get list where each element is [value, weight]. each item is its index. items start with index 1!
def getCapacityAndItems(filename):
	file_by_line = open(filename, 'r').read().split('\n')
	list_by_items = [line.split(' ') for line in file_by_line]
	items = [[int(item[0]), int(item[1])] for item in list_by_items]
	return items[0][1], items[0][0], items

# TESTING
print(getOptimalValueForKnapsack('items_small.txt'))