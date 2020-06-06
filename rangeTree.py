#range tree implementation - not completed

def printLeaf(root):
  if root is None:
    return
  if root.left is None and root.right is None:
    print(root.data)
    return
  if root.left is not None:
    printLeaf(root.left)
  if root.right is not None:
    printLeaf(root.right)

def printLevelOrder(root): 
      
    # Base case 
    if root is None: 
        return
    # Create an empty queue for level order traversal 
    q = [] 
      
    # Enqueue root and initialize height 
    q.append(root) 
          
    while q: 
      
        # nodeCount (queue size) indicates number 
        # of nodes at current lelvel. 
        count = len(q) 
          
        # Dequeue all nodes of current level and  
        # Enqueue all nodes of next level  
        while count > 0: 
            temp = q.pop(0) 
            print(temp.data, end = ' ') 
            if temp.left: 
                q.append(temp.left) 
            if temp.right: 
                q.append(temp.right) 
  
            count -= 1
        print(' ') 


class OneDeeNode:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None


class HigherDeeNode:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None
		self.other = None

class OneDeeRangeTree:
	def __init__(self, data=None):
		self.root = OneDeeNode()
		if data != None:
			self.add(data, self.root)
	def add(self, node, root):
		if self.root.data == None:
			self.root.data = node.data
			self.root.left = OneDeeNode(node.data)
			return

		if root.data == None:
			root.data = node.data
			return

		temp = root

		if node.data[0] <= temp.data[0]:
			if temp.left is None:
				temp.left = OneDeeNode()
				temp.right = OneDeeNode(temp.data)
				temp.data = node.data
			self.add(node, temp.left)
		if node.data[0] > temp.data[0]:
			if temp.right is None:
				temp.right = OneDeeNode()
				temp.right.left = OneDeeNode(node.data)
			self.add(node, temp.right)

	def find(self, root, data):
		if root.data[0] == data:
			return root
		elif data > root.data[0]:
			self.find(root.right, data)
		elif data <= root.data[0]:
			self.find(root.left, data)
	
	def rangeSearch(self, start, end, results, root):
		if root is None:
			return
		if root.left is None and root.right is None:
			if start <= root.data[0] <= end:
				results.append(root.data)
				return
		if root.left is not None:
			self.rangeSearch(start, end, results, root.left)
		if root.right is not None:
			self.rangeSearch(start, end, results, root.right)

class TwoDeeRangeTree:
	def __init__(self):
		self.root = HigherDeeNode()
	
	def add(self, node, roott):
		if self.root.data == None:
			self.root.data = node.data
			self.root.left = HigherDeeNode(node.data)
			self.root.left.other = OneDeeRangeTree(node)
			self.root.other = OneDeeRangeTree(node)
			return
		
		if roott.data == None:
			roott.data = node.data
			return
		
		temp = roott

		if node.data[1] <= temp.data[1]:
			if temp.left is None:
				temp.left = HigherDeeNode()
				temp.right = HigherDeeNode(temp.data)
				temp.data = node.data
				if temp.other == None:
					temp.other = OneDeeRangeTree()
			temp.other.add(node, temp.other.root)
			self.add(node, temp.left)
		if node.data[1] > temp.data[1]:
			if temp.right is None:
				temp.right = HigherDeeNode()
				temp.right.other = OneDeeRangeTree(node)
				temp.right.left = HigherDeeNode(node.data)
			temp.other.add(node, temp.other.root)
			self.add(node, temp.right)

lines = open("data.txt", "r")

a = TwoDeeRangeTree()


for line in lines:
	employeeInfo = line.split()
	node = HigherDeeNode(employeeInfo)
	a.add(node, a.root)

printLeaf(a.root)
