# this code finds strongly connected components in a directed graph usign Kosaragu's two pass algorithm

def setup(fileName):
	fileByLine = open(fileName, 'r').read().split('\n')
	normal_graph = {}
	reverse_graph = {}

	# get graphs as adj matrix
	for line in fileByLine:
		string_list = line.split(' ')
		int_list = [int(string_list[0]), int(string_list[1])]

		# normal graph
		if int_list[0] in normal_graph:
			normal_graph[int_list[0]].append(int_list[1])
		else:
			normal_graph[int_list[0]] = [int_list[1]]

		# reverse graph
		if int_list[1] in reverse_graph:
			reverse_graph[int_list[1]].append(int_list[0])
		else:
			reverse_graph[int_list[1]] = [int_list[0]]

	return normal_graph, reverse_graph

def findSCC(fileName):

	# get adj_list of graphs
	normal_graph, reverse_graph = setup(fileName)

	# needed data
	class _data:
		t = 0
		s = None
		leader = {}
		explored = set()
		finish_time = {}

	data = _data()

	# first past DFS Loop
	DFS_loop(reverse_graph, reverse_graph.keys(), data)
	
	# second processing list
	timing_list = sorted(data.finish_time, key=data.finish_time.get, reverse=True)
	
	# seond past DFS loop
	data.explored = set()
	DFS_loop(normal_graph, timing_list, data)
	print(data.leader)

# DFS
def DFS(graph, node, data):
	data.explored.add(node)
	data.leader[node] = data.s
	for elem in graph[node]:
		if elem not in data.explored and elem in graph:
			DFS(graph, elem, data)
	data.t += 1
	data.finish_time[node] = data.t

# DFS Loop
def DFS_loop(graph, processList, data):
	for elem in processList:
		if elem not in data.explored:
			data.s = elem
			DFS(graph, elem, data)

findSCC('smallgraph.txt')