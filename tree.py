import math
# Method Translation:
# t.isLeaf(node) => t.leaf, returns a boolean
# t.get(node) => t.value, returns the value of the node
# t.getchildren(node) => t.children, returns an array of tree objects

class tree:

	# Initial Values
	# t: parent
	def __init__(self,t,value):
		self.parent = t
		self.children = []
		if type(value) == str: # BRANCH
			self.label = value
			self.leaf = False
			self.value = math.inf
		if type(value) == int: # LEAF
			self.label = "l"
			self.leaf = True
			self.value = value

		if t != 0: # connect child to parent
			t.addChild(self)

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

def readStruct(file):
	f = open(file,"r")
	line = f.readline()
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

	return root

# t = tree(0,"i")
# q = tree(t,"q")
# w = tree(t,"w")
# l = tree(q,"l")
# k = tree(q,"k")
# o = tree(w,"o")
# l1 = tree(l,6)
# l2 = tree(l,5)
# l3 = tree(k,1)
# l4 = tree(k,2)
# l5 = tree(o,1)
# l6 = tree(o,3)

t = readStruct("alphabet_small.txt")
d = readStruct("alphabet_medium.txt")



print("Small Tree")
t.printTree()
print("Medium Tree")
d.printTree()
