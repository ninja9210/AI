class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F


def dfs(node):
	if node is not None:
		print(node.value) 
		dfs(node.left)    
		dfs(node.right)   


print("DFS Traversal of the tree:")
dfs(A)
