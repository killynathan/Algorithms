
class UnionFind(object):
	def __init__(self, size):
		self.tree = [x for x in range(0, size)]
		self.size = [1 for x in range(0, size)]

	def print(self):
		print(self.tree)
		print(self.size)

	def root(self, node):
		i = node
		while i != self.tree[i]:
			self.tree[i] = self.tree[self.tree[i]]
			i = self.tree[i]
		return i

	def find(self, node1, node2):
		return self.root(node1) == self.root(node2)

	def union(self, node1, node2):
		i = self.root(node1)
		j = self.root(node2)
		if i == j:
			return
		if self.size[i] < self.size[j]:
			self.tree[i] = j
			self.size[j] += self.size[i]
		else:
			self.tree[j] = i
			self.size[i] += self.size[j]

def get_max_spacing(filename, num_of_clusters):
	num_nodes, edge_list = get_num_of_nodes_and_edges(filename)
	UF = UnionFind(num_nodes + 1) # want to start at 1, ignore 0
	cluster_count = num_nodes
	edge_list_index = 0
	while cluster_count > num_of_clusters:
		node1, node2, weight = edge_list[edge_list_index]
		edge_list_index += 1
		if not UF.find(node1, node2):
			UF.union(node1, node2)
			cluster_count -= 1

	
	for edge in edge_list:
		if not UF.find(edge[0], edge[1]):
			print(edge)
			return edge[2]



# get descending by weight list of edges in the form [vertex1, vertex2, weight]
def get_num_of_nodes_and_edges(filename):
	list_by_line = open(filename, 'r').read().split('\n')
	edge_list = []
	for line in list_by_line[1:]:
		edge_list.append([int(x) for x in line.split(' ')])
	num_nodes = int(list_by_line[0])
	edge_list.sort(key=lambda t: t[2])
	return num_nodes, edge_list

test = UnionFind(6)
test.union(1,2)
test.union(2,3)
test.union(3,4)

get_max_spacing('weightedGraph.txt', 4)