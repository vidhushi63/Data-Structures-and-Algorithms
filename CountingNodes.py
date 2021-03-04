class node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class Tree:
    def __init__(self):
        self.root=None

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ,")
        self.inorder(root.right)
   
    def totalNode(self,root):
        if root is None:
            return 0
        return 1+self.totalNode(root.left)+self.totalNode(root.right)
    def numFullNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return self.numFullNodes(root.left) + self.numFullNodes(root.right) + (1 if root.left is not None and root.right is not None else 0);
    def leafNode(self,root):
        if root is None:
            return 0
        if root.left is None and  root.right is None:
            return 1
        return self.leafNode(root.left)+self.leafNode(root.right)
    def nonLeafNode(self,root):
        if root is None:
            return 0
        if root.left is not None and root.right is not None:
            return self.totalNode(self.root)-self.leafNode(self.root)
ob=Tree()
ob.root=node(1)
ob.root.left=node(2)
ob.root.right=node(3)
ob.root.left.left=node(4)
ob.root.left.right=node(5)
ob.root.right.left=node(6)
ob.root.right.right=node(7)
ob.root.left.left.left=node(8)
ob.root.left.left.right=node(9)
ob.root.right.left.left=node(10)
ob.root.right.right.right=node(9)

print("\nInorder")
ob.inorder(ob.root)
print()
print("Number Of Full Nodes:", end = " ")
print(ob.numFullNodes(ob.root))
print()
print("Total Number of Nodes:",end=" ")
print(ob.totalNode(ob.root))
print("leaf Nodes:",end=" ")
print(ob.leafNode(ob.root))
print("Non leaf  Nodes:",end=" ")
print(ob.nonLeafNode(ob.root))