from RangeTree_2D import TwoDeeRangeTree
from Node import HigherDeeNode
import csv

#with open('employee-salary-data-1.csv') as csv_file:
#        csv_reader = csv.reader(csv_file, delimiter=',')
#        line_count = 0
#        for row in csv_reader:
#                if line_count == 0:
#                        print(f'Column names are {", ".join(row)}')
#                        line_count += 1
#                else:
#                        print(f'\t{row[0]} {row[1]} {row[2]}.')
#                        line_count += 1
#        print(f'Processed {line_count} lines.')


class ThreeDeeRangeTree:
    def __init__(self):
        self.root = HigherDeeNode()
        self.n = 0

        with open('employee-salary-data-1.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count > 1000:
                        break
                    
                    if line_count == 0:
                            #print(f'Column names are {", ".join(row)}')
                            pass
                    else:
                        employeeInfo = [row[1], row[6], row[8], row[2], row[3], row[4]]
                        node = HigherDeeNode(employeeInfo)
                        self.add(node, self.root)
                        #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                        #line_count += 1
                    line_count += 1
                print(f'Processed {line_count} lines.')

#       lines = open("data.txt", "r")

#       for line in lines:
#           employeeInfo = line.split()
#           node = HigherDeeNode(employeeInfo)
#           self.add(node, self.root)
    def add(self, node, roott):
        if self.root.data == None:
            self.root.data = node.data
            self.root.left = HigherDeeNode(node.data)
            self.root.left.other = TwoDeeRangeTree(node)
            self.root.other = TwoDeeRangeTree(node)
            self.n += 1
            return
        
        if roott.data == None:
            roott.data = node.data
            self.n += 1
            return
        
        temp = roott

        if node.data[2] <= temp.data[2]:
            if temp.left is None:
                temp.left = HigherDeeNode()
                temp.right = HigherDeeNode(temp.data)
                if temp.other == None:
                    temp.other = TwoDeeRangeTree()
                temp.other.add(HigherDeeNode(temp.data), temp.other.root)
                temp.data = node.data
            temp.other.add(node, temp.other.root)
            self.add(node, temp.left)
        if node.data[2] > temp.data[2]:
            if temp.right is None:
                temp.right = HigherDeeNode()
                temp.right.other = TwoDeeRangeTree(node)
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
        if start_two <= int(float(roott.data[2])) <= end_two:
            roott.other.rangeSearch(start_two, end_two, start_one, end_one, start_zero, end_zero, results, roott.other.root)
            return
        if start_two > int(float(roott.data[2])):
            self.rangeSearch(start_two, end_two, start_one, end_one, start_zero, end_zero, results, roott.right)
        if end_two < int(float(roott.data[2])):
            self.rangeSearch(start_two, end_two, start_one, end_one, start_zero, end_zero, results, roott.left)
    def get_all(self, results):
        self.rangeSearch(float('-inf'), float('inf'), float('-inf'), float('inf'), float('-inf'), float('inf'), results, self.root)


##Print Leafs/Trees - For debugging purpose

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
