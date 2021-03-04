class node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def preorder(self,root):
        if root is None:
            return 
        print(root.data,end=" ,")
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ,")
        self.inorder(root.right)
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=", ")
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
print("PreOrder")
ob.preorder(ob.root)
print("\nPostOrder")
ob.postorder(ob.root)
print("\nInorder")
ob.inorder(ob.root)
