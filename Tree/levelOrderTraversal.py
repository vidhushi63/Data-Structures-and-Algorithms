#level order traversal
from collections import deque
class node:
    def __init__(self,data):
        self.left=self.right=None
        self.data=data
class BFS:
    def __init__(self):
        self.root=None 
    def show(self,root):
        if root is None:
            return None
        queue=deque()
        BFS=[]
        queue.append(self.root)
        
        while queue:
            size=len(queue)
            for i in range (size):
                curr=queue.popleft()
                BFS.append(curr.data)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                    
                print(curr.data, end = " ")
ob=BFS()
ob.root=node(1)
ob.root.left=node(6)
ob.root.right=node(3)
ob.root.left.left=node(49)
ob.root.left.right=node(5)
ob.show(ob.root)