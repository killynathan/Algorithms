import BellmanFord
import dijkstra
import copy

def getAllPairsShortestPath(filename):
	# data structs
	n, edges = BellmanFord.getGraph(filename)
	minPath = float('inf')

	edgesTemp = copy.deepcopy(edges)
	
	# add new vertex s with edges of weight 0 pointing to all vertices to get new G'
	for i in range(1,n + 1):
		edgesTemp.append([n + 1, i, 0])
	
	# Run bellman ford on new graph from s & detect cycle
	# A = weighting for each vertex as shortest path from s
	A = BellmanFord.findShortestPathsFromSource(n + 1, edgesTemp, n + 1)
	if A == 'negative cycle':
		return 'negative cycle'
	
	# reweight each edge u->v as weight of edge plus A of u minus A of v
	for edge in edges:
		edge[2] = edge[2] + A[edge[0]] - A[edge[1]]
	
	# run Djikstra for each vertex 
	adj_list = getAdjList(edges)
	for v in range(1, n + 1):
		dist = dijkstra.findShortestPath(adj_list, n, v, A)
	
		if dist < minPath:
			minPath = dist
	
	return minPath

def getAdjList(edges):
	adj_list = {}

	for edge in edges:
		if edge[0] in adj_list:
			adj_list[edge[0]].append([edge[1], edge[2]])
		else:
			adj_list[edge[0]] = [[edge[1], edge[2]]]
	return adj_list

print(getAllPairsShortestPath('g3.txt'))