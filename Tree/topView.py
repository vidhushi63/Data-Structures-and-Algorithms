class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
        
class Sol:
    def __init__(self):
        self.root=None
    def topView(self,root):
        q=[]
        q.append((root,0))
        d={}
        
        while q:
            root,level=q.pop(0)
            if level not in d:
                d[level]=root.data
            if root.left:
                q.append((root.left,level-1))
                
            if root.right:
                q.append((root.right,level+1))
                
        for i in sorted(d):
            print(d[i],end="  ")
ob=Sol()
ob.root=Node(1)
ob.root.right=Node(2)
ob.root.right.right=Node(5)
ob.root.right.right.left=Node(3)
ob.root.right.right.right=Node(6)
ob.root.right.right.left.right=Node(4)
ob.topView(ob.root)
