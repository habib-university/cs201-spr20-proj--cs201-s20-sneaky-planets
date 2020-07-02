from Node import OneDeeNode, HigherDeeNode
from RangeTree_1D import OneDeeRangeTree

class TwoDeeRangeTree:
	def __init__(self, node = None):
		self.root = HigherDeeNode()
		self.n = 0
		if node != None:
			self.add(node, self.root)

	def add(self, node, roott):
		if self.root.data == None:
			self.root.data = node.data
			self.root.left = HigherDeeNode(node.data)
			self.root.left.other = OneDeeRangeTree(node)
			self.root.other = OneDeeRangeTree(node)
			self.n += 1
			return
		
		if roott.data == None:
			roott.data = node.data
			self.n += 1
			return
		
		temp = roott

		if node.data[1] <= temp.data[1]:
			if temp.left is None:
				temp.left = HigherDeeNode()
				temp.right = HigherDeeNode(temp.data)
				if temp.other == None:
					temp.other = OneDeeRangeTree()
				temp.other.add(OneDeeNode(temp.data), temp.other.root)
				temp.data = node.data
			temp.other.add(node, temp.other.root)
			self.add(node, temp.left)
		if node.data[1] > temp.data[1]:
			if temp.right is None:
				temp.right = HigherDeeNode()
				temp.right.other = OneDeeRangeTree(node)
				temp.right.left = HigherDeeNode(node.data)
			temp.other.add(node, temp.other.root)
			self.add(node, temp.right)

	def rangeSearch(self, start_two, end_two, start_one, end_one, start_zero, end_zero, results, roott):
		if start_one > end_one or start_zero > end_zero:
			print("Invalid Queries!")
			return
		if roott is None:
			print("No Results")
			return
		if start_one <= int(float(roott.data[1])) <= end_one:
			roott.other.rangeSearch(start_two, end_two, start_one, end_one, start_zero, end_zero, results, roott.other.root)
			return
		if start_one > int(float(roott.data[1])):
			self.rangeSearch(start_two, end_two, start_one, end_one, start_zero, end_zero, results, roott.right)
		if end_one < int(float(roott.data[1])):
			self.rangeSearch(start_two, end_two, start_one, end_one, start_zero, end_zero, results, roott.left)

