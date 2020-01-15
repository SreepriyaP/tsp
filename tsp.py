from queue import PriorityQueue
class City:
	def __init__(self, id, x, y):
		self.id = id
		self.x = int(x)
		self.y = int(y)
	def cityDistance(self, other):
		return (((abs(self.x - other.x)**2) + (abs(self.y - other.y)**2))**0.5)

class State:
	def __init__(self, path = [], distance = 0, todo = []):
		self.path = path
		self.distance = distance
		self.todo = todo
	def __lt__(self, other):
		return self.distance < other.distance
	def setDistance(self, distance):
		self.distance = distance
	def setTodo(self, cityList):
		self.todo = []
		for i in cityList:
			if i not in self.path:
				self.todo.append(i)
	def getPath(self):
		cities = []
		# print(self.path)
		for i in self.path:
			cities.append(i.id)
		return cities
	def getTodo(self):
		cities = []
		for i in self.todo:
			cities.append(i.id)
		return cities
	def pathDistance(self):
		dist = 0  
		for i in range(len(self.getPath()) - 1):
			dist += self.path[i].cityDistance(self.path[i+1])
		return dist

def getCities(filename):
	f = open(filename, "r")
	cities = []
	for line in f:
		words = line.split()
		cities.append(City(words[0], words[1], words[2]))
	return cities

def getCityInfo(cityList):
	distances = [[0 for x in range(len(cityList))] for y in range(len(cityList))]
	for i in range(len(cityList)):
		for j in range(len(cityList)):
			distances[i][j] = cityList[i].cityDistance(cityList[j])
	return distances



def childrenstates(state, citylist):
	children = []
	for i in state.todo:
		# print(i)
		child = State(state.path[:-1]+ [i] + [state.path[-1]])
		child.setDistance(child.pathDistance())
		child.setTodo(cityList)
		children.append(child)
	return children


def a_star():
	while not pq.empty():  #len(currnode.getTodo()) is not 0:
		priority_of_node, currnode = pq.get()
		children = childrenstates(currnode, cityList)
		for child in children:
			pq.put((child.distance, child))
	return currnode.getPath()


cityList = getCities("cityInfo.txt")
pq = PriorityQueue()
state1 = State([cityList[0], cityList[0]], cityList[0].cityDistance(cityList[0]))
state1.setTodo(cityList)
pq.put((0, state1))
print(a_star())

# class Graphs:
# 	def __init__(self):
# 		self.V = []
# 		self.graph = []
# 	def addEdge(self, edge):
# 		if edge[0] in self.V and edge[1] in self.V:
# 			return
# 		if edge[0] not in self.V:
# 			self.V.append(edge[0])
# 		if edge[1] not in self.V:
# 			self.V.append(edge[1])
# 		self.graph.append(edge)
		


# def Boruvka(component):
# 	graphList = []
# 	for k in component:
# 		for j in k.graph:
# 			print("j", j)
# 			added = False
# 			for i in graphList:
# 				if j[0] in i.V or j[1] in i.V:
# 					i.addEdge(j)
# 					print("i graph", i.graph)
# 					added = True
# 					break
# 		if added is False:
# 			f = Graphs()
# 			f.addEdge(j)
# 			graphList.append(f)
# 	return graphList

# comps = getCityInfo(cityList)
# cities = [0,1,2,3,4]
# def getCheapest(comps, cities):
# 	minimums = []
# 	for i in cities:
# 		comps[i][i] = None
# 		j = comps[i].index(min(filter(lambda x: x is not None, comps[i])))
# 		g = Graphs()
# 		g.addEdge([i,j])
# 		minimums.append(g)
# 	return minimums

# print(getCheapest(comps, cities))
# g = Boruvka(getCheapest(comps, cities))
# print(g)
