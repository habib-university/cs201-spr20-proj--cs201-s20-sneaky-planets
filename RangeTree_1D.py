from Node import OneDeeNode
import numpy as np
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

    def returnLeafsWithRange(self, start_one, end_one, start, end, results, root):
        if root == None:
            return
        if root.left is None and root.right is None:
            if start <= int(root.data[0]) <= end and start_one <= int(root.data[1]) <= end_one:
                results.append(root.data)
                return
        if root.left is not None and int(root.data[0]) >= start:
            self.returnLeafsWithRange(start_one, end_one, start, end, results, root.left)
        if root.right is not None and int(root.data[0]) <= end:
            self.returnLeafsWithRange(start_one, end_one, start, end, results, root.right)

    def rangeSearch(self, start_one, end_one, start, end, results, root):
        if root is None:
            print("No Results")
            return
        if start <= int(root.data[0]) <= end:
            self.returnLeafsWithRange(start_one, end_one, start, end, results, root)
            return
        if start > int(root.data[0]):
                self.rangeSearch(start_one, end_one, start, end, results, root.right)
        if end < int(root.data[0]):
                self.rangeSearch(start_one, end_one, start, end, results, root.left)
