#range tree implementation - not completed

class NodeForOneDee:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None



#simple binary tree ( only add function )
#TODO: necessary changes to convert it into a one dimensional range tree 

class OneDeeRangeTree: 
    
    def __init__(self):
      self.root = NodeForOneDee()
    
    def add(self, node, root):
      
      if root.data == None:
        root.data = node.data
        return
      
      temp = root

      if node.data[0] <= temp.data[0]:
        if temp.left is None:
          temp.left = NodeForOneDee()
          temp.left.left = NodeForOneDee(node.data)
          temp.left.right = NodeForOneDee(temp.data)
        self.add(node, temp.left)
      if node.data[0] > temp.data[0]:
        if temp.right is None:
          temp.right = NodeForOneDee()
          temp.right.left = NodeForOneDee(node.data)
        self.add(node, temp.right)

    def find(self, start, end, results, root):
      if root is None:
        return
      if root.left is None and root.right is None:
        if start <= root.data[0] <= end:
          results.append(root.data)
          return
      if root.left is not None:
        self.find(start, end, results, root.left)
      if root.right is not None:
        self.find(start, end, results, root.right)

class TwoDeeRangeTree:
  def __init__(self):
    self.root = 


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



check = SimpleTree()
check.add(NodeForOneDee(5), check.root)
check.add(NodeForOneDee(3), check.root)
check.add(NodeForOneDee(10), check.root)

ans = []

check.find(5, 10, ans, check.root)

# printLeaf(check.root)
print(ans)


# Final Implementation of a 4D Range Tree
# TODO: Functions to be implemented:
# - init
# - add
# - remove
# - find
# class RangeTree:
#     def __init__():
#         self.root = None
#         lines = open("data.txt", "r")
#         order_by_id = OneDimRT("id")
#         for line in lines:
#             employeeInfo = line.split()
#             employee = Node(data) #data is a list where 0: id, 1: age, 2: position, 3: salary, 4: name
            

