import math
# Method Translation:
# t.isLeaf(node) => t.leaf, returns a boolean
# t.get(node) => t.value, returns the value of the node
# t.getchildren(node) => t.children, returns an array of tree objects

class tree:

	# Initial Values
	# t: parent
	def __init__(self,parent,value):
		self.parent = parent
		self.children = []
		if type(value) == str: # BRANCH
			self.label = value
			self.leaf = False
			self.value = math.inf
		if type(value) == int: # LEAF
			self.label = "l"
			self.leaf = True
			self.value = value

		if parent != 0: # connect child to parent
			parent.addChild(self)

	def addChild(self,t): # add a child to a parents children
		self.children.append(t)

	def printChildren(self): # simple print children with their parents
		for i in self.children:
			if i.leaf:
				print(i.parent.label+"->"+str(i.value),end =" ")
				# print(str(i.value),end =" ")
			else:
				print(i.parent.label+"->"+i.label, end =" ")
				# print(i.label, end =" ")
			if i == self.children[len(self.children)-1]:
				print("")

	def printTree(self):
		if self.parent == 0:
			print(self.label)
		if self.leaf:
			return
		self.printChildren()
		for i in self.children:
			i.printTree() # simple print of the tree

# readStruct: reads the structure of a tree from a given txt file
def readStruct(file):
	f = open(file,"r")
	tL = []
	for line in f:
		line = line.split(" ")
		treeStr = line[1].split("),(")
		nodes = []
		parents = {}

		# ROOT
		rootL = treeStr[0][2:].split(",")
		label = rootL[0]
		root = tree(0,rootL[0])
		parents[label] = root
		# Second
		label = rootL[1]
		second = tree(root,label)
		parents[label] = second


		for i in treeStr[1:-1]:
			temp = i.split(",")
			try:
				parent = parents[temp[0]]
				value = int(temp[1])
				node = tree(parent,value)
			except:
				parent = parents[temp[0]]
				node = tree(parent,temp[1])
				parents[temp[1]] = node

		temp = treeStr[len(treeStr)-1][:-3].split(",")
		parent = parents[temp[0]]
		value = int(temp[1])
		node = tree(parent,value)

		tL.append(root)
	return tL
