#range tree implementation - not completed

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

#simple binary tree
#TODO: necessary changes to convert it into a one dimensional range tree 

class SimpleTree: 
    def __init__(self):
      self.root = Node()
    def add(self, node, root):
      if root.data == None:
        root.data = node.data
        # root.left = Node(node.data)
        return
      temp = root
      if node.data <= temp.data:
        if temp.left is None:
          temp.left = Node()
        self.add(node, temp.left)
      if node.data > temp.data:
        if temp.right is None:
          temp.right = Node()
        self.add(node, temp.right)


# to print the tree ( for debugging )
def printLevelOrder(root): 
  if root is None: 
    return
  q = [] 
  q.append(root) 
  while q: 
    count = len(q) 
    while count > 0: 
      temp = q.pop(0) 
      print(temp.data, end = ' ') 
      if temp.left: 
        q.append(temp.left) 
      if temp.right: 
        q.append(temp.right) 

      count -= 1
    print(' ') 

check = SimpleTree()
check.add(Node(5), check.root)
check.add(Node(3), check.root)
check.add(Node(10), check.root)

printLevelOrder(check.root)


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
            

