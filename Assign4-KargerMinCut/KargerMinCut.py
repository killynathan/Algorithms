# imports
import random, copy

# random contraction algoritm
# finds the min cuts in a graph using Karger's algorithm given enough iterations
def RCA(adj_list):

	#base case: two or nodes left
	while len(adj_list) > 2:

		# pick a random edge
		# this is not completely uniformly random. can do better but does it matter due to the number of trials?
		nodeIKeep = random.choice(adj_list.keys())
		nodeIMerge = random.choice(adj_list[nodeIKeep])
		
		listOfNodeIMerge = adj_list[nodeIMerge]
		
		#merge two vertices 
		adj_list[nodeIKeep] += listOfNodeIMerge

		# redirect edges going to merged node to node i keep
		for elem in listOfNodeIMerge:
			adj_list[elem].remove(nodeIMerge)
			adj_list[elem].append(nodeIKeep)

		# delete self loops
		while nodeIKeep in adj_list[nodeIKeep]:
			adj_list[nodeIKeep].remove(nodeIKeep)

		del adj_list[nodeIMerge]

	for elem in adj_list:
		return len(adj_list[elem])

def operateRCA(file, numberOfOperations):
	adj_list = getAdjListFromTxtFile(file)
	i = 0
	min_cut = 100000
	while i < numberOfOperations:
		data = copy.deepcopy(adj_list)
		num = RCA(data)
		if num < min_cut:
			min_cut = num
		i += 1
	return min_cut

# testing

# get representation of graph using list of lists. first element in is placeholder. 
# starts at 1
def getAdjListFromTxtFile(file):
	temp = open(file, "r").read().split('\n')
	graph = {}
	for row in temp:
		row_string = row.split('\t')
		if row_string[len(row_string) - 1] is '':
			del row_string[len(row_string) - 1]
		row_int = []
		for elem in row_string:
			row_int.append(int(elem))
		graph[row_int[0]] = row_int[1:]
	return graph


print(operateRCA("AdjacencyList.txt", 100))