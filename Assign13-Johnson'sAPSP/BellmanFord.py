import math

def findShortestPathsFromSource(numOfVertices, edges, source):
	# constant
	INF = 99999

	# used for stopping early
	listIsSameAsBefore = True

	# get data structs
	#numOfVertices, edges = getGraph2(filename) # !!!!!!! 1 vs 2
	A = [INF]*(numOfVertices + 1) # vertices indexed starting from 1
	A[source] = 0 # source node

	for i in range(numOfVertices + 1):
		listIsSameAsBefore = True
		for u,v,w in edges:
			if (A[u] + w < A[v]):
				A[v] = A[u] + w
				listIsSameAsBefore = False
		if listIsSameAsBefore:
			break
		elif (i == numOfVertices):
			return 'negative cycle'

	return A


# return numOfVertices and [[vertex 1, v 2, weight of edge], ...]
def getGraph(filename):
	graph = []
	lines = open(filename).read().split('\n')
	for line in lines:
		values = line.split(' ')
		graph.append([int(i) for i in values])
	return graph[0][0], graph[1:]

def getGraph2(filename):
	graph = []
	lines = open(filename).read().split('\n')
	for line in lines:
		edges = line.split('\t')
		for edge in edges[1:(len(edges) - 1)]:
			edgeContent = edge.split(',')
			graph.append([int(edges[0]), int(edgeContent[0]), int(edgeContent[1])])

	return 200, graph

# n, test = getGraph('g3.txt')

# print(findShortestPathsFromSource(n, test, 1))

