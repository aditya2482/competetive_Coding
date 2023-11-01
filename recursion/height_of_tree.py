count_l=1
count_r=1
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
   
    def PrintTree(self,root):
        print("inside_main,root to be printed", root.data)
        print(root.data)
        if root.left:
            print("Inside_left -- root is ",root.data)
            self.PrintTree(root.left)
        if root.right:
            print("inside_right,root is ",root.data)
            self.PrintTree(root.right)
    
    # By aman Bhaiya
    
    def get_height(self,root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return max(left_height,right_height)+1


root = Node(10)
root.left = Node(5)
#root.left.right = Node(7)
root.left.left = Node(15)
root.right = Node(2)
root.left.left.right = Node(6)
# root.PrintTree(root)
root.right.right= Node(1)
root.right.right.right= Node(0)
root.left.left.right.left = Node(6)
root.right.right.right.left = Node(6)
root.right.right.right.left.right = Node(8)
print(root.get_height(root))
