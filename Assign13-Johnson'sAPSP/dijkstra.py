# use dijkstra's to find shortest path for all elements using 
# a heap.

import heapq

def findShortestPath(adj_list, numOfVertices, source, A):
	# heap = [[value, key], ....]
	# heap_dict is there so we can access elements in the heap at constant time
	#	it is simply references to all elements in the heap.
	# 	We need this because we need to update the values of elements in the heap
	#	as we traverse the graph.
	
	heap, heap_dict, min_dist_dict = initializa_data_structures(adj_list, numOfVertices, source)
	firstPop = True;
	minDist = float('inf')
	
	# while heap_dict is nonempty, get greedy pick one by one
	while len(heap_dict) > 0:
		# get element with smallest greedy score
		vertex, value = pop(heap, heap_dict)
		
		# update dict with shortest distance of the popped vertes
		if firstPop:
			firstPop = False;
		else: 
			min_dist_dict[vertex] = value
			trueValue = value - A[source] + A[vertex]
			if (trueValue < minDist):
				minDist = trueValue
		
		# update neighboring vertices of popped vertex that have not been chosed yet
		if vertex in adj_list:
			for vertex_and_weight in adj_list[vertex]:
				vertex, edge_weight = vertex_and_weight
				if vertex in heap_dict:
					new_value = value + edge_weight
					update(vertex_and_weight, heap_dict, heap, new_value)

	return minDist

def create_adj_list(fileName):
	list_by_line = open(fileName, "r").read().split('\n')
	list_by_entry = []
	for line in list_by_line:
		list_by_entry.append(line.split('\t'))
	list_by_datapair = []
	adj_list = {}
	for entry in list_by_entry:
		row_of_datapairs = []
		for datapair in entry[1:len(entry) - 1]:
			datapair_string = datapair.split(',')
			datapair_int = [int(i) for i in datapair_string]
			row_of_datapairs.append(datapair_int)
		adj_list[int(entry[0])] = row_of_datapairs
	return adj_list

def initializa_data_structures(adj_list, numOfVertices, source):
	heap = []
	# for vertex in adj_list:
	# 	print(vertex)
	# 	if vertex is source:
	# 		heapq.heappush(heap, [0, vertex])
	# 	else:
	# 		heapq.heappush(heap, [1000000, vertex])

	for i in range(1, numOfVertices + 1):
		if i == source:
			heapq.heappush(heap, [0, i])
		else:
			heapq.heappush(heap, [1000000, i])

	heap_dict = {i[1]: i for i in heap}
	min_dist_dict = {}
	return heap, heap_dict, min_dist_dict

def pop(heap, heap_dict):
	while len(heap) > 0:
		value, vertex = heapq.heappop(heap)
		if (vertex is not 'deleted'):
			del heap_dict[vertex]
			return vertex, value

def delete(vertex, heap_dict):
	heap_dict[vertex][1] = 'deleted' # just marking since we dont want to heapify - O(N)

def update(vertex_and_weight, heap_dict, heap, new_value):
	vertex, weight = vertex_and_weight
	# doing this so actual element in heap is being deleted as heap and heap_dict refer to same elemnt
	delete(vertex, heap_dict) 
	new_vertex = [min(new_value, heap_dict[vertex][0]),vertex]
	heap_dict[vertex] = new_vertex
	heapq.heappush(heap, new_vertex)

