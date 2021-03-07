class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class Sol:
    def __init__(self):
        self.root=None
    def sec_min(self,root):
        a=set()
        def inorder(root):
            if root is None:
                return None
            a.add(root.data)
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        if len(a)<2:
            return -1
        firstmin=10000
        secmin=10000
        thirdmin=10000
        for i in a:
            if i<firstmin:
                thirdmin=secmin
                secmin=firstmin
                firstmin=i
            elif i<secmin:
                thirdmin=secmin
                secmin=i
            elif i<thirdmin:
                thirdmin=i
        print(firstmin,secmin,thirdmin)
        
        
  
ob=Sol()
ob.root=Node(2)
ob.root.left=Node(8)
ob.root.right=Node(4)
ob.root.left.right=Node(5)
ob.root.right.right=Node(6)
ob.root.left.left=Node(9)
ob.root.right.left=Node(0)
ob.sec_min(ob.root)