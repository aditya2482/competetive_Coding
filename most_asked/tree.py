class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self):
       root = Node(0)
       self.helpi(root,0)
       return root
       
   def helpi(self,root,level_count):
    #   print(level_count)
       if level_count == 2:
           
           return root
           
       if root.data == 0:
           root.left = Node(0)
           root.right = Node(1)
       if root.data == 1:
           root.left = Node(1)
           root.right = Node(0)
           
       self.helpi(root.left,level_count+1)
       self.helpi(root.right,level_count+1)

   def hi(self,root):
       print(root.right.right.data)
       
    
       
               
        
        
#    def printTree(self):
#        self.hi(self.root)

    
    
    
    
           



# Use the insert method to add nodes
a = Node(None)
root = a.insert()
a.hi(root)
a.solution(root)